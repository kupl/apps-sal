class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        dq = deque([(A, 0)])
        cnt = 0
        N = len(A)
        seen = set()
        while dq:
            length = len(dq)

            for _ in range(length):
                curr, idx = dq.popleft()
                lst = list(curr)

                for i in range(idx, N):
                    if lst[i] != B[i]:
                        for j in range(i + 1, N):
                            if lst[j] != B[j] and lst[j] == B[i]:
                                lst[i], lst[j] = lst[j], lst[i]
                                temp = ''.join(lst)
                                if temp == B:
                                    return cnt + 1
                                if temp not in seen:
                                    seen.add(temp)
                                    dq.append((temp, i + 1))
                                lst[i], lst[j] = lst[j], lst[i]
                        break

            cnt += 1

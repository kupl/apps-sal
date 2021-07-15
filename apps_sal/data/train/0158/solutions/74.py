class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A==B: return 0
        N = len(A)
        dq = deque([(A, 0)])
        cnt = 0
        seen = {A}
        while dq:
            length = len(dq)
            
            for _ in range(length):
                a, idx = dq.popleft()
                
                for i in range(idx, N):
                    if a[i]!=B[i]:
                        break
                else:
                    return cnt
                
                lst = list(a)
                for j in range(i+1, N):
                    if a[j]!=B[j] and a[j]==B[i]:
                        lst[j], lst[i] = lst[i], lst[j]
                        state = ''.join(lst)
                        if state not in seen:
                            seen.add(state)
                            dq.append((state, i+1))
                        lst[j], lst[i] = lst[i], lst[j]
                        if a[i]==B[j]:
                            break
                            
            cnt += 1


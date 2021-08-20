class Solution:

    def kSimilarity(self, A, B):
        out = 0
        q = deque()
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            else:
                q.append([list(B), i])
                break

        def find_neighbors(arr, i):
            e = A[i]
            nei = []
            for x in range(i + 1, len(arr)):
                if arr[x] == e:
                    nei.append(x)
            return nei
        while q:
            for _ in range(len(q)):
                (cur, idx) = q.popleft()
                while idx < len(cur):
                    if cur[idx] == A[idx]:
                        idx += 1
                    else:
                        break
                if idx == len(cur):
                    return out
                else:
                    nei = find_neighbors(cur, idx)
                    for n in nei:
                        new = cur[:]
                        new[n] = cur[idx]
                        q.append([new, idx + 1])
            out += 1
        return out

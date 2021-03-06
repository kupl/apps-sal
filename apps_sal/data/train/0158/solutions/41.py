class Solution:

    def kSimilarity(self, A, B):

        def find_neighbors(arr, i):
            e = A[i]
            nei = []
            for x in range(i + 1, len(arr)):
                if arr[x] == e:
                    nei.append(x)
            return nei
        q = deque()
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            else:
                q.append([list(B), i])
                break
        l = 0
        while q:
            for x in range(len(q)):
                e = q.popleft()
                y = e[1]
                while y < len(e[0]):
                    if e[0][y] == A[y]:
                        y += 1
                    else:
                        break
                if y == len(e[0]):
                    return l
                else:
                    nei = find_neighbors(e[0], y)
                    for n in nei:
                        new_e = e[0][:]
                        new_e[n] = e[0][y]
                        q.append([new_e, y + 1])
            l += 1
        return l

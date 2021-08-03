class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        N = len(A)

        def dfs(A, B, pos):
            if A == B:
                return 0

            while A[pos] == B[pos]:
                pos += 1

            minCnt = float('inf')
            for i in range(pos + 1, N):
                if B[i] == A[pos] and B[i] != A[i]:
                    B[i], B[pos] = B[pos], B[i]
                    tmp = dfs(A, B, pos + 1) + 1
                    minCnt = min(tmp, minCnt)
                    B[i], B[pos] = B[pos], B[i]

            return minCnt

        return dfs(list(A), list(B), 0)

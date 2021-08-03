class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)

        dp = [[2 for c in range(n)] for r in range(n)]

        visited = {}
        res = 2

        for i in range(n - 1):
            for j in range(i + 1, n):

                prev = A[i] * 2 - A[j]

                if prev < 0 or prev not in visited:
                    continue

                dp[i][j] = dp[visited[prev]][i] + 1

                res = max(res, dp[i][j])

            visited[A[i]] = i

        return res

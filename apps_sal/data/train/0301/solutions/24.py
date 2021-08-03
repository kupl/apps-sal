from collections import defaultdict


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        vals_A = defaultdict(list)
        for i in range(len(A)):
            vals_B = defaultdict(list)
            for j in range(len(B)):
                dp[i + 1][j + 1] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1])
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)

                for pos in vals_A[B[j]]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[pos][j] + 1)
                for pos in vals_B[A[i]]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][pos] + 1)

                vals_B[B[j]] += [j]

            vals_A[A[i]] += [i]

        return dp[len(A)][len(B)]

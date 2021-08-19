class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(5)]
        md = 10 ** 9 + 7
        for i in range(5):
            dp[i][0] = 1
        (A, E, I, O, U) = (0, 1, 2, 3, 4)
        for i in range(1, n):
            dp[E][i] = (dp[E][i] + dp[A][i - 1]) % md
            dp[A][i] = (dp[A][i] + dp[E][i - 1]) % md
            dp[I][i] = (dp[I][i] + dp[E][i - 1]) % md
            dp[A][i] = (dp[A][i] + dp[I][i - 1]) % md
            dp[E][i] = (dp[E][i] + dp[I][i - 1]) % md
            dp[O][i] = (dp[O][i] + dp[I][i - 1]) % md
            dp[U][i] = (dp[U][i] + dp[I][i - 1]) % md
            dp[I][i] = (dp[I][i] + dp[O][i - 1]) % md
            dp[U][i] = (dp[U][i] + dp[O][i - 1]) % md
            dp[A][i] = (dp[A][i] + dp[U][i - 1]) % md
        ans = 0
        for i in range(5):
            ans = (ans + dp[i][-1]) % md
        return ans

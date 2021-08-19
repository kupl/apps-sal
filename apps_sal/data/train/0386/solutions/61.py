class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # drawing graph
        # a -> e
        # e -> a, i
        # i -> a, e, o, u
        # o -> i, u
        # u -> a

        # 'a' can follow {'e', 'i', 'u'}
        # 'e' can follow {'a', 'i'}
        # 'i' can follow {'e', 'o'}
        # 'o' can follow {'i'}
        # 'u' can follow {'i', 'o'}

        mod = 10**9 + 7
        count = 0

        # cols = the 5 vowels, rows = length of string
        # i,j coord denotes num of valid strings of length i
        # col 0 = a, 1 = e, 2, = i, 3 = o, 4 = u
        dp = [[0 for i in range(5)] for j in range(n + 1)]

        for i in range(5):
            dp[1][i] = 1

        for i in range(1, n):
            dp[i + 1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % mod
            dp[i + 1][1] = (dp[i][0] + dp[i][2]) % mod
            dp[i + 1][2] = (dp[i][1] + dp[i][3]) % mod
            dp[i + 1][3] = (dp[i][2]) % mod
            dp[i + 1][4] = (dp[i][2] + dp[i][3]) % mod

        for i in range(5):
            count = (count + dp[n][i]) % mod

        return count

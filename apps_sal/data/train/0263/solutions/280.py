class Solution:

    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        mapper = {1: [8, 6], 2: [7, 9], 3: [8, 4], 4: [0, 9, 3], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = [[0] * 10 for _ in range(N)]
        MM = 10 ** 9 + 7
        for i in range(10):
            if i == 5:
                continue
            dp[0][i] = 1

        def searching(s, i):
            if dp[s][i] > 0:
                return dp[s][i]
            for k in mapper[i]:
                dp[s][i] += searching(s - 1, k)
                dp[s][i] = dp[s][i] % MM
            return dp[s][i]
        for i in range(10):
            if i == 5:
                continue
            searching(N - 1, i)
        return sum(dp[N - 1]) % MM

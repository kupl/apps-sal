class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(i)] for i in rollMax]

        def sum_dp(j=-1):
            return sum(sum(x) for index, x in enumerate(dp) if index != j)

        for i in range(6):
            dp[i][0] = 1

        for i in range(n - 1):
            dp2 = [[0 for _ in range(i)] for i in rollMax]
            for j in range(6):
                max_len = len(dp[j])
                for k in range(max_len - 1, 0, -1):
                    dp2[j][k] = dp[j][k - 1]
                dp2[j][0] = sum_dp(j)
            dp = dp2

        return sum_dp() % 1000000007

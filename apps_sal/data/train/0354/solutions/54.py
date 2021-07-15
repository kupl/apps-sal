class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][k] means after several rolls, the number of sequence that ends with i for k times.
        mod = 10**9 + 7
        dp = [[0, 1] + [0] * 14 for i in range(6)]
        for _ in range(n - 1):
            dp2 = [[0] * 16 for i in range(6)]
            # update the dp table
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    # all choices
                    for j in range(6):
                        # if same, only not > max
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        # if not, add anyway
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod

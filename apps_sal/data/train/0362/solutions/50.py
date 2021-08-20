class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        max_hat = max([item for hat in hats for item in hat])
        n = len(hats)
        dp = [[0 for _ in range(2 ** n)] for _ in range(max_hat + 1)]
        for i in range(max_hat + 1):
            dp[i][0] = 1
        for i in range(1, max_hat + 1):
            for j in range(2 ** n):
                acc = 0
                for k in range(n):
                    cur_bit = 1 << k
                    if j & cur_bit != 0 and i in hats[k]:
                        acc += dp[i - 1][j - cur_bit]
                dp[i][j] = (dp[i - 1][j] + acc) % 1000000007
        return dp[max_hat][2 ** n - 1]

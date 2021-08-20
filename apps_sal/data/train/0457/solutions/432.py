class Solution:

    def coinChange(self, coins: List[int], a: int) -> int:
        if a == 0:
            return 0
        dp = [-1 for i in range(a + 1)]
        dp[0] = 1
        coins.sort()
        for i in range(1, len(coins) + 1):
            for j in range(1, a + 1):
                if coins[i - 1] == j:
                    dp[j] = 1
                else:
                    c = -1
                    if j - coins[i - 1] > 0 and dp[j - coins[i - 1]] != -1:
                        c = dp[j - coins[i - 1]] + 1
                    d = dp[j]
                    if c != -1 and d != -1:
                        dp[j] = min(c, d)
                    elif c == -1 and d != -1:
                        dp[j] = d
                    elif c != -1:
                        dp[j] = c
        if dp[a] == -1:
            return -1
        else:
            return dp[a]

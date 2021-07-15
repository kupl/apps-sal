class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        T = len(coins)
        dp = [0 for i in range(amount + 1)]
        for n in range(1, amount + 1):
            dp[n] = math.inf
            for i in range(T):
                if (n - coins[i] >= 0):
                    subProbSol = dp[n - coins[i]]
                    dp[n] = min(dp[n], subProbSol + 1)
        if dp[amount] == math.inf : return -1
        else : return (dp[amount])


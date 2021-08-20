class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount + 1):
            for i in range(n):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1


'\nclass Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        int Max = amount + 1;\n        vector<int> dp(amount + 1, Max);\n        dp[0] = 0;\n        for (int i = 1; i <= amount; i++) {\n            for (int j = 0; j < coins.size(); j++) {\n                if (coins[j] <= i) {\n                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);\n                }\n            }\n        }\n        return dp[amount] > amount ? -1 : dp[amount];\n    }\n};\n'

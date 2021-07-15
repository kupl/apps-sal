class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        summary = 0
        result = [float('inf')]*(amount+1)
        result[0] = 0
        while summary <= amount:
            if result[summary] != -1:
                for i in coins:
                    if summary + i <= amount and result[summary] + 1 < result[summary + i]:
                        result[summary + i] = result[summary] + 1
            summary += 1
        return -1 if result[amount] == float('inf') else result[amount]


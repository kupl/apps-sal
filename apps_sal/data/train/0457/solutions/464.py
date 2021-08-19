class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {i: [] for i in range(1, amount + 1)}
        coins.sort()
        for intermediate_amount in range(1, amount + 1):
            '\n                basic algorithm: \n                    - for each number, start from the end of the coins list\n                    - subtract the given denomination\n                    - check if the hash map has an entry for the amount - denomination\n                    - use the first possible configuration\n                    - if all possibilities are exhausted, no denomination exists\n            '
            for denom in reversed(coins):
                if intermediate_amount == denom:
                    dp[intermediate_amount] = [denom]
                    break
                elif denom < intermediate_amount and dp[intermediate_amount - denom] != []:
                    if dp[intermediate_amount] == [] or len(dp[intermediate_amount]) > len(dp[intermediate_amount - denom]) + 1:
                        dp[intermediate_amount] = dp[intermediate_amount - denom] + [denom]
        return len(dp[amount]) if len(dp[amount]) > 0 else -1

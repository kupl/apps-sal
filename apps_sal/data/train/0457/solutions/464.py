class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {i: [] for i in range(1, amount + 1)}
        coins.sort()
        for intermediate_amount in range(1, amount + 1):
            '''
                basic algorithm: 
                    - for each number, start from the end of the coins list
                    - subtract the given denomination
                    - check if the hash map has an entry for the amount - denomination
                    - use the first possible configuration
                    - if all possibilities are exhausted, no denomination exists
            '''
            for denom in reversed(coins):
                if intermediate_amount == denom:
                    dp[intermediate_amount] = [denom]
                    break  # we know this is the minimum number of denoms, we can stop here
                elif denom < intermediate_amount and dp[intermediate_amount - denom] != []:
                    # update the array if it's the first time OR if len(dp[intermediate_amount]) > len(dp[intermediate_amount - denom]) + 1
                    if dp[intermediate_amount] == [] or len(dp[intermediate_amount]) > len(dp[intermediate_amount - denom]) + 1:
                        dp[intermediate_amount] = dp[intermediate_amount - denom] + [denom]
        return len(dp[amount]) if len(dp[amount]) > 0 else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change_memo(coins, amount, memo):
            if amount not in memo:
                if amount == 0:
                    best = 0
                elif amount < 0:
                    best = -1
                else:
                    best = None
                    for c in coins:
                        res = change_memo(coins, amount-c, memo)
                        if res == -1:
                            continue
                        if (best is None) or (res < best):
                            best = res
                    if best is None:
                        best = -1
                    else:
                        best += 1
                memo[amount] = best
                
            return memo[amount]
        
        memo = {}
        change_memo(coins, amount, memo)
        return memo[amount]

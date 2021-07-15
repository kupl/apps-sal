class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or not coins:
            return 0
        
        minlst = [float('inf')] * (amount + 1)
        n = len(minlst)
        minlst[0] = 0

        for i in range(1,n):
            for denom in coins:
                remainder = i - denom
                if remainder < 0:
                    continue

                newsmallest = min(minlst[remainder] + 1, minlst[i])
                minlst[i] = newsmallest
        return -1 if minlst[-1] == float('inf') else minlst[-1]

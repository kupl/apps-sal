'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_num = [float('inf') for _ in range(amount + 1)]
        min_num[0] = 0
        
        for c in coins:
            for s in range(c, amount + 1):
                min_num[s] = min(min_num[s], min_num[s - c] + 1)
                
        return -1 if min_num[amount] == float('inf') else min_num[amount]
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res, seen, curr = 0, set(), {c for c in coins if c <= amount}
        while curr:
            res += 1
            if amount in curr:
                return res
            seen |= curr
            tmp = {n+c for n in curr for c in coins}
            curr = {t for t in tmp if t not in seen and t <= amount}
        return -1

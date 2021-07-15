class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        if not coins:
            return -1
        
        memo = {}
            
        stack = [amount]
        l = 0
        while stack:
            tmp = []
            for remain in stack:
                if remain < 0:
                    continue
                
                for coin in coins:
                    nxt = remain-coin
                    if nxt == 0:
                        return l+1
                    if nxt in memo:
                        continue
                    else:
                        memo[nxt] = 1
                    tmp += [nxt]
            stack = tmp
            l += 1
        return -1
            
                
                
                



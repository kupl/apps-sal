class Solution:
    def coinChange(self, coins, amount):
        if not coins: return -1
        if not amount: return 0
        if amount in coins: return 1
        
        C = tuple(sorted(coins,reverse=True))
        length, self.ans = len(C)-1, float('inf')
        
        def find(coin, step, target):
            now_coin = C[coin]
            q, r = divmod(target,now_coin)
            
            if not r:
                self.ans = min(self.ans, step+q)
            elif coin < length and step+q+1 < self.ans:
                coin += 1
                for j in range(q,-1,-1):
                    find(coin, step+j, target-j*now_coin)
            
        find(0, 0, amount)
        return -1 if self.ans==float('inf') else self.ans

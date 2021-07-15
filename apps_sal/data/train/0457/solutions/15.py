class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([])
        seen = set()
        
        queue.append((0,0))
        
        while queue:
            summ, num_coins = queue.popleft()
            if summ == amount:
                return num_coins
            
            for coin in coins:
                if summ+coin<=amount and summ+coin not in seen:
                    queue.append((summ+coin, num_coins+1))
                    seen.add(summ+coin)
        
        return -1
#         coins = sorted(coins, reverse=True)
#         memo = {}
#         def coinChangeRec(index, amount):
#             if amount == 0:
#                 return 0
#             if amount < 0 or index == len(coins):
#                 return math.inf
#             if (index, amount) in memo:
#                 return memo[(index, amount)]
            
#             withCoin = coinChangeRec(index, amount - coins[index]) + 1
#             withoutCoin = coinChangeRec(index+1, amount)
            
#             memo[(index, amount)] = min(withCoin, withoutCoin)
#             return min(withCoin, withoutCoin)
                     
#         minCoins = coinChangeRec(0, amount)
#         if minCoins == math.inf:
#             return -1
#         return minCoins
    


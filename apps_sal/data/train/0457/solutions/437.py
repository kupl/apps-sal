class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        # min_coins = [math.inf]*(amount+1)
        # min_coins[0] = 0
        # for coin in coins:
        #     for amount in range(coin,amount+1):
        #         min_coins[amount] = min(min_coins[amount], min_coins[amount-coin]+1)
        # # print(min_coins)
        # if min_coins[-1] == math.inf:
        #     return -1
        # else: return min_coins[-1]
        cache = {}
        def subproblem(i,t):
            if t == 0:
                return 0
            if (i,t) in cache:
                return cache[(i,t)]
            val = coins[i]
            if val > t:
                choice_take = math.inf
            elif val == t:
                choice_take = 1
            else:
                choice_take = 1 + subproblem(i,t-val)
                
            if i == 0:
                choice_leave = math.inf
            else:
                choice_leave = subproblem(i-1,t)
            optimal = min(choice_take, choice_leave)
            cache[(i,t)] = optimal
            return optimal
        
        mincoins = subproblem(len(coins)-1, amount)
        if mincoins == math.inf:
            return -1
        else:
            return mincoins


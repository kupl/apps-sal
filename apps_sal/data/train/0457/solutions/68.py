class Solution:
#     def do_bf(self, coins, amount, index):
#         if amount == 0:
#             return 0
#         n = len(coins)
#         if n <= index:
#             return math.inf

#         count_keeping_element = math.inf
#         if coins[index] <= amount:
#             temp = self.do_bf(coins, amount - coins[index], index)
#             if temp != math.inf:
#                 count_keeping_element = temp + 1

#         count_skipping_element = self.do_bf(coins, amount, index + 1)
#         return min(count_keeping_element, count_skipping_element)

#     def do_td_mem(self, cache, coins, amount, index):

#         if amount == 0:
#             return 0

#         if len(coins) <= index:
#             return math.inf

#         if cache[index][amount] == math.inf:
#             count_keeping_element = math.inf
#             if coins[index] <= amount:
#                 temp = self.do_td_mem(cache, coins, amount - coins[index], index)
#                 if temp != math.inf:
#                     count_keeping_element = temp + 1

#             count_skipping_element = self.do_td_mem(cache, coins, amount, index + 1)
#             cache[index][amount] = min(count_keeping_element, count_skipping_element)
#         return cache[index][amount]


    
    def do_du_tab(self, coins, amount):
        dp_tab = [math.inf for _ in range(amount+1)]
        dp_tab[0] = 0
        for a in range(1, amount+1):
            potential = []
            
            for coin in coins: 
                potential.append(dp_tab[a-coin]+1)
            
            dp_tab[a] = min(potential)
            
        return dp_tab[-1] if dp_tab[-1]!=float('inf') else -1

    
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        if len(coins) == 0:
            return 0
        if amount == 0:
            return 0
  
        c = [coin for coin in coins if coin <= amount]
        if len(c) == 0:
           return -1
        #c.sort(reverse=True)

        return self.do_du_tab(c, amount)


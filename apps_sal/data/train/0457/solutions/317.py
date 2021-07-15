import math
from functools import lru_cache 

class Solution:

       
    
    ### Iterative DFS
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        
        stack = [(0,0)]  # sum, coinCount
        answer = math.inf
        
        # !! n.b, sorting small->big so stack processing searches largest first
        sortedCoins = sorted(coins) 
        # !! n.b. prune search tree to prevent re-searching same sums
        visited = set()
        
        while stack:
            # print(sorted(stack, reverse=True))
            (sum, coinCount) = stack.pop()
            
            if (sum, coinCount) in visited:
                pass
            elif coinCount >= answer:
                pass
            elif sum == amount:
                answer = min(answer,coinCount)
            elif sum > amount:
                pass
            else:
                for c in sortedCoins:
                    if ( 
                        (sum+c) <= amount and
                        # !! n.b. ensure still possible to beat best answer 
                        # !! with this coin
                        amount < (sum + (c*(answer-coinCount)))
                    ):
                        stack.append((sum+c, coinCount+1))
                        
            visited.add((sum, coinCount))
                
        if answer == math.inf:
            return -1
        else:
            return answer
    
    
    
#     ### Iterative DFS.  Brute force won't finish on large trees
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         stack = [(0,0)]    # (sum, count)
#         # visited = set()
#         answer = math.inf
        
#         while stack:
#             node = stack.pop()
#             # print(node)
            
#             if node[0] == amount:
#                 answer = min(answer, node[1])
#             elif node[0] > amount:
#                 pass
#             else:
#                 for coin in coins:
#                     stack.append( (node[0]+coin, node[1]+1)  )
                    
#         if answer == math.inf:
#             return -1
#         else:
#             return answer
        
        
#     ### Recursive DFS with memoization
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         @lru_cache(maxsize=None)
#         def dfs(remainder):
#             if remainder < 0:
#                 return math.inf
#             elif remainder == 0:
#                 return 0
#             else:
#                 least = math.inf
#                 for coin in coins:
#                     least = min(least, dfs(remainder - coin) + 1)
#                 return least
        
#         res = dfs(amount)
#         if res == math.inf:
#             return -1
#         else:
#             return res
    
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         def backtrack(remainder):
#             # print(remainder)
#             if remainder in memo:
#                 return memo[remainder]
#             elif remainder < 0:
#                 return math.inf
#             elif remainder == 0:
#                 memo[remainder] = 0
#                 return memo[remainder]
#             else:
#                 least = math.inf
#                 for coin in coins:
#                     least = min(least, backtrack(remainder - coin) + 1)
#                 memo[remainder] = least
#                 return memo[remainder]    
        
#         memo = collections.defaultdict(int)
#         res = backtrack(amount)
#         if res == math.inf:
#             return -1
#         else:
#             return res
        
        
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins or amount < 0:
#             return -1
        
#         @lru_cache(maxsize=None)
#         def dfs(sum, count):
#             # print(\"sum:{}, count:{}\".format(sum, count))
#             if count >= self.ans:
#                 return
#             elif sum == amount:
#                 self.ans = min(self.ans, count)
#                 return
#             elif sum > amount:
#                 return
#             else:
#                 for c in sortedCoins:
#                     dfs(sum+c, count+1)
                    
#         sortedCoins = sorted(coins, reverse=True)
#         self.ans = math.inf
#         dfs(0,0)
#         if self.ans == math.inf:
#             return -1
#         else:
#             return self.ans
        
    
#     ### BFS
#     def coinChange(self, coins: List[int], amount: int) -> int:  
#         if not coins or amount < 0:
#             return -1
        
#         visited = [False]*(amount+1)
#         parentNodes = [0]
#         level = -1
        
#         while parentNodes:
#             level += 1
#             childNodes = []
#             for node in parentNodes:
#                 if visited[node]:
#                     pass
#                 elif node == amount:
#                     return level
#                 elif node > amount:
#                     pass
#                 else:
#                     for c in coins:
#                         if node+c <= amount:
#                             childNodes.append(node+c)
#                 visited[node] = True      
                
#             parentNodes = childNodes
            
#         return -1

    
#     ### Dynamic programming
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         maxint = math.inf
        
#         # one slot for each amount, up to amount. 
#         dp = [0] + [maxint]*amount
        
#         for i in range(1,amount+1):
#             dp[i] = min([(1+dp[i-c]) for c in coins if i>=c] + [maxint])
            
#         if dp[amount] == math.inf:
#             return -1
#         else:
#             return dp[amount]
        
    
### Recursive w/memoization    
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         sortedCoins = sorted(coins, reverse=True)
#         result = self.recurse(amount, tuple(sortedCoins))
        
#         if result == math.inf:
#             result = -1
        
#         return result
        
#     @lru_cache(maxsize=None)
#     def recurse(self, amount: int, coins: tuple) -> int:
#         # print(amount)
#         if amount < 0:
#             return math.inf
#         elif amount == 0:
#             return 0
#         else:
#             least = math.inf
#             for c in coins:
#                 val = self.recurse(amount-c, coins)
#                 if val < math.inf:
#                     # print('{} = {}'.format(amount-c, val))
#                     least = min(least, val)
#             return least + 1
                


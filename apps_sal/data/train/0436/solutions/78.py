import math
from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        if n < 2: return n
        queue = deque()
        running_count = n
        min_days = 0
        queue.append((min_days,n))
        seen = set()
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                local_min, local_n = queue.popleft()
                seen.add(local_n)
                if local_n < 0: continue
                if local_n == 0: return local_min
                    
                if local_n%2 == 0 and local_n-local_n//2 not in seen:
                    queue.append((local_min+1,(local_n-local_n//2)))
                if local_n%3 == 0 and local_n-2*(local_n//3) not in seen:
                    queue.append((local_min+1,(local_n-2*(local_n//3))))
                queue.append((local_min+1,local_n-1))
        return min_days
        
        
        
# SEMI OPTIMIZED SOLUTION         
#     def minDays(self, n: int) -> int:
#         if n < 2: return n
#         dp = [math.inf for _ in range(n+1)]
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 2
        
#         for i in range(3,n+1):
#             c1,c2,c3 = math.inf,math.inf,math.inf
#             if i%2 == 0:
#                 c1 = dp[i - i//2]+1
#             if i%3 == 0:
#                 c2 = dp[i - 2*(i//3)]+1
#             c3 = dp[i-1]+1
#             dp[i] = min(c1,c2,c3)
            
#         return dp[n]
        
        
        
        
        
        
        
        
        
        
        
        
# ##### BRUTE FORCE        ####
#     def minDays(self, n: int) -> int:
#         self.dic = {}
#         return self.helper(n,0)
    
#     def helper(self, days_left, count):
#         if days_left == 0: return count
#         c1,c2,c3 = math.inf, math.inf, math.inf
#         c1 = self.helper(days_left-1,count+1)
#         if days_left %2 ==0:
#             c2 = self.helper(days_left//2,count+1)
#         if days_left % 3 ==0:
#             c3 = self.helper(days_left//3,count+1)
        
#         return min(c1,c2,c3)



#     def minDays(self, n: int) -> int:
#         if n < 2: return n
#         dp = [math.inf for _ in range(n+1)]
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 2
        
#         for i in range(3,n+1):
#             c1,c2,c3 = math.inf,math.inf,math.inf
#             if i%2 == 0:
#                 c1 = dp[i - i//2]+1
#             if i%3 == 0:
#                 c2 = dp[i - 2*(i//3)]+1
#             c3 = dp[i-1]+1
#             dp[i] = min(c1,c2,c3)
            
#         return dp[n]


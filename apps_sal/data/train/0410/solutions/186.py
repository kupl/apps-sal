from collections import defaultdict
# import heapq
from operator import itemgetter 
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_dict = defaultdict(int)
        
        def cal_power(n):
            nonlocal power_dict
            
            if n in list(power_dict.keys()):
                return power_dict[n]-1
            if n==1:
                return 0
            if n%2==0:
                n = n/2
            elif n%2==1:
                n = 3*n+1
                
            power_dict[n] = cal_power(n)+1
            return power_dict[n]
        lst = []
        for i in range(lo,hi+1):
            lst.append((cal_power(i),i))
        
        lst = sorted(lst,key = itemgetter(0))
        return lst[k-1][1]

        # print(lst)
#         heapq.heapify(lst)
        
#         for i in range(k):
#             ans = heapq.heappop(lst)
        
#         return ans[1]  
    
    
#         @lru_cache(None)
#         def power(x):
#             if x == 1:
#                 return 0
#             if x % 2 == 0:
#                 return 1 + power(x // 2)
#             return 1 + power(3 * x + 1)

#         return sorted(range(lo, hi+1), key=power)[k-1]
    
                
                


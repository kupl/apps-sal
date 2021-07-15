# from itertools import combinations 
# import sys
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
#         if D == 1:
#             return sum(weights)
        
#         all_comb = combinations(range(1,len(weights)), D-1)
        
#         res = sys.maxsize
#         for comb in all_comb:
#             cap = 0
#             # print(comb)
#             for i in range(len(comb) + 1):
#                 if i == 0:
#                     cap = max(cap, sum(weights[:comb[i]]))
#                 elif i == len(comb):
#                     cap = max(cap, sum(weights[comb[i-1]:]))
#                 else:
#                     cap = max(cap, sum(weights[comb[i-1]:comb[i]]))
#             res = min(res, cap)
#         return(res)

        lower = max(weights)
        upper = sum(weights)
        
        while abs(lower - upper) > 1:
            mid = (lower + upper) // 2
            # print(lower, upper)
            if self.is_shipped(mid, weights, D):
                upper = mid
            else:
                lower = mid
        
        if lower == upper or self.is_shipped(lower, weights, D):
            return lower
        else:
            return upper
                
    def is_shipped(self, cap, weights, D):
        tmp = 0
        count = 1
        for i in range(len(weights)):
            tmp += weights[i]
            if tmp == cap:
                count += 1
                tmp = 0
            elif (tmp > cap):
                count += 1
                tmp = weights[i]
        return count <= D

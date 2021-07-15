class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rt = 0
        prof = 0
        maxRt = 0
        maxProf = 0
        wait = 0
        i = 0
        onborad = 0
        while wait > 0 or i < len(customers):
            if i < len(customers):
                wait += customers[i]
                i += 1
            onboard = min(4, wait)
            wait -= onboard
            prof = prof + onboard * boardingCost - runningCost
            rt += 1
            if maxProf < prof:
                maxProf = prof
                maxRt = rt
            
        if maxProf > 0 :
            return maxRt
        else:
            return -1 
        
#         pro = 0
#         curpro = 0 
#         wait = 0
#         on = 0
#         j = 0 
#         for i, n in enumerate(customers):
#             if n >= 4:
#                 wait += n - 4
#                 on += 4
#             else:
#                 on += n
#             j += 1
#             curpro = on* boardingCost - j *runningCost
#             if curpro < 0:
#                 ans = -1
#             elif pro < curpro:
#                 pro = max(pro, curpro)
#                 ans = j
    
#         while wait > 0:
#             if wait >= 4:
#                 wait -= 4
#                 on += 4
#             else:
#                 on += wait
#                 wait = 0
#             j += 1
#             curpro = on* boardingCost - j*runningCost
#             if curpro < 0:
#                 ans = -1
#             elif pro < curpro:
#                 if j > 300:
#                     print(on, wait, pro, curpro, j)
#                 ans = j
#                 pro = max(pro, curpro)
        
#         return ans



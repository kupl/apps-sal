class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        most = pnl = waiting = 0
        for i, x in enumerate(customers):
            waiting += x  # more people waiting in line
            waiting -= (chg := min(4, waiting))  # boarding
            pnl += chg * boardingCost - runningCost
            if most < pnl:
                ans, most = i + 1, pnl
        q, r = divmod(waiting, 4)
        if 4 * boardingCost > runningCost:
            ans += q
        if r * boardingCost > runningCost:
            ans += 1
        return ans
# class Solution:
#     profit = 0
#     rotations = 0 #number of rotations
#     def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
#         \"\"\"
#             Input: customers = [8,3], boardingCost = 5, runningCost = 6

#                                     const                           const
#             FORMULA: profit = (numofppl * boardingcost) - (rotations * runningCost)

#             need to find: numofppl and rotations
#         \"\"\"
#         numofppl = 0
#         pplwaiting = 0
#         i = 0
#         while i < len(customers):
#             toboard = 0
#             #if there are people waiting
#             if pplwaiting > 0:
#                 if pplwaiting > 4
#                     toboard += 4
#                     pplwaiting -=4
#                     continue #maxed
#                 else:
#                     toboard += pplwaioting
#                     pplwaiting = 0

#             pplneededforfull = 4-pplwaiting
#             #if pplwaiting was not enough for full group, look @ current customer group
#             if customers[i] > pplneededforfull: #add ppl waiting to numofppl

#                 numofppl += 4
#                 pplwaiting = customers[i] - 4 #subtract 4
#                 continue

#             #if current group still has people waiting
#             if customers[i]>0:
#                 numofppl += customers[i] #add ppl waiting to numofppl
#                 customers[i] = 0


#             i+=1 #rotate gonda
#         charge(4)
#         charge(3)
#         print(self.profit)

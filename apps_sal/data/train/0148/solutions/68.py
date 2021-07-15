# # Fisrt solution
# def createListOfProfitDiff(profit, difficulty):
#     profit_diff = []
#     for i in range(len(profit)):
#         profit_diff.append((profit[i], difficulty[i]))
#     return profit_diff
        
        
        
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
#         profit_diff = createListOfProfitDiff(profit, difficulty)
#         profit_diff.sort(key=lambda x:x[0])
#         worker2 = sorted(worker)

#         maxprofit = 0
#         for i in range(len(profit_diff)-1, -1, -1):
#             for j in range(len(worker2) -1, -1, -1):
#                 if profit_diff[i][1]> worker2[j]:
#                     break
#                 else:
#                     maxprofit += profit_diff[i][0]
#                     worker2.pop(j)
#         return maxprofit
# Second solution
def createListOfProfitDiff(profit, difficulty):
    profit_diff = []
    for i in range(len(profit)):
        profit_diff.append((profit[i], difficulty[i]))
    return profit_diff
        
        
        
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
#         profit_diff = createListOfProfitDiff(profit, difficulty)
#         profit_diff.sort(key=lambda x:x[0])
#         worker2 = sorted(worker)

#         maxprofit = 0
#         i = len(profit_diff) -1
#         j = len(worker2)-1
#         while i<len(profit_diff) and j <len(worker2) and i>-1 and j>-1:
#             if profit_diff[i][1]> worker2[j]:
#                 i-=1
#             else:
#                 maxprofit += profit_diff[i][0]
#                 worker2.pop(j)
#                 j-=1
#         return maxprofit

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w = sorted(worker)
        w.reverse()
        dp = []
        for i in range(len(profit)):
            dp.append((profit[i], difficulty[i]))
        dp.sort(key =  lambda x:x[0])
        dp.reverse()

        i = 0
        count = 0
        for p in dp:
            while i<len(w) and p[1] <= w[i]:
                count += p[0]
                i+=1
        return count
                


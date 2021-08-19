class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
#         table = [[None]*len(satisfaction) for i in range(len(satisfaction))]
#         for i in range(len(satisfaction)):
#             for j in range(i,len(satisfaction)):
#                 table[i][j] = satisfaction[j]*(i+1)
#         bestSat = float('-inf')
#         for i in range(len(satisfaction)):
#             row = i
#             col = len(satisfaction)-1
#             currSat = 0
#             while row >= 0:
#                 currSat += table[row][col]
#                 row -= 1
#                 col -= 1
#             bestSat = max(bestSat,currSat)
#         return max(bestSat,0)

        bestSat = float('-inf')
        for i in range(len(satisfaction)):
            n = len(satisfaction) - 1
            numItems = i + 1
            numAdded = 0
            currSat = 0
            while numAdded <= numItems:
                currSat += satisfaction[n - numAdded] * (numItems - numAdded)
                numAdded += 1
            bestSat = max(bestSat, currSat)
        return max(bestSat, 0)

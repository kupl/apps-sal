class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        table = [[None]*len(satisfaction) for i in range(len(satisfaction))]
        for i in range(len(satisfaction)):
            for j in range(len(satisfaction)):
                if i > j:
                    continue
                table[i][j] = satisfaction[j]*(i+1)
        bestSat = float('-inf')
        for i in range(len(satisfaction)):
            row = i
            col = len(satisfaction)-1
            currSat = 0
            while row >= 0:
                currSat += table[row][col]
                row -= 1
                col -= 1
            bestSat = max(bestSat,currSat)
        return max(bestSat,0)

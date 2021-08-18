class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

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

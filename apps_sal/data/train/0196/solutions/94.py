class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxHere = currentMax = float('-inf')
        minHere = currentMin = float('inf')
        for i in A:
            currentMax = i + max(0, currentMax)
            currentMin = i + min(0, currentMin)
            maxHere = max(currentMax, maxHere)
            minHere = min(currentMin, minHere)
        print(maxHere, minHere)
        if minHere == sum(A) and 0 not in A:
            return maxHere
        return max(maxHere, sum(A)-minHere)

class Solution:
    def isValidCapacity(self, weights, D, capacity):
        totalDays = 1
        i = 0
        runningSum = 0

        for i in range(len(weights)):
            if runningSum + weights[i] > capacity:
                runningSum = weights[i]
                totalDays += 1
            else:
                runningSum += weights[i]

        return totalDays <= D
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            if self.isValidCapacity(weights, D, mid):
                high = mid
            else:
                low = mid + 1

        return low
        


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        totalCusts = 0
        for idx, custs in enumerate(customers):
            if grumpy[idx] == 0:
                totalCusts += customers[idx]
                customers[idx] = 0
        rollingSum = 0
        maxSum = 0
        for i, n in enumerate(customers):
            rollingSum += n
            if i - X >= 0:
                rollingSum -= customers[i - X]
            maxSum = max(maxSum, rollingSum)
        return maxSum + totalCusts

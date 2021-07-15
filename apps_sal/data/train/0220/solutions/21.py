class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        gain = 0
        for i in range(X):
            if grumpy[i]:
                gain += customers[i]
        max_gain = gain
        for i in range(X, len(customers)):
            gain = gain + customers[i]*grumpy[i] - customers[i-X]*grumpy[i-X]
            max_gain = max(max_gain, gain)
        statify = 0
        for i in range(len(customers)):
            statify += customers[i]*(1-grumpy[i])
        return statify + max_gain

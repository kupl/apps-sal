class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        res = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        best_gain = sum([customers[i] * grumpy[i] for i in range(X)])
        gain = best_gain
        for i in range(X, n):
            gain += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            best_gain = max(best_gain, gain)
        return res + best_gain

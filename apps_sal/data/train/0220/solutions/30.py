class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        n = len(customers)
        res = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        best_gain = sum([customers[i] * grumpy[i] for i in range(k)])
        gain = best_gain
        for i in range(k, n):
            gain += customers[i] * grumpy[i] - customers[i - k] * grumpy[i - k]
            best_gain = max(gain, best_gain)
        return res + best_gain

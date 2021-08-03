class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0

        n = sum(customers[:X])
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
        return n + t

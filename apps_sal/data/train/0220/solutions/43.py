class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        (lb, ub) = (0, X - 1)
        total = sum([customers[i] * (1 - grumpy[i]) for i in range(len(customers))])
        saved = 0
        for i in range(X):
            if grumpy[i]:
                saved += customers[i]
        ans = total + saved
        while ub + 1 < len(grumpy):
            (lb, ub) = (lb + 1, ub + 1)
            if grumpy[lb - 1]:
                saved -= customers[lb - 1]
            if grumpy[ub]:
                saved += customers[ub]
            ans = max(ans, total + saved)
        return ans

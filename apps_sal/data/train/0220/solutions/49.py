class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        windowMax = 0
        curr = 0
        for i in range(len(customers)):
            curr += ((grumpy[i]) * customers[i])
            if i >= X:
                curr -= ((grumpy[i - X]) * customers[i - X])
            windowMax = max(windowMax, curr)
        return satisfied + windowMax


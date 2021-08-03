class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfy = sum(cust for cust, grump in zip(customers, grumpy) if grump == 0)
        max_extra = extra = sum(cust for cust, grump in zip(customers[:X], grumpy[:X]) if grump == 1)
        start, end = 0, X
        n = len(customers)
        while end < n:
            extra += grumpy[end] * customers[end]
            extra -= grumpy[start] * customers[start]
            max_extra = max(max_extra, extra)
            start += 1
            end += 1
        return satisfy + max_extra

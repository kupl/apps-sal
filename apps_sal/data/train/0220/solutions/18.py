class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        grumpy, grum_sum, cus_sum = [i ^ 1 for i in grumpy], [0] * len(customers), [0] * len(customers)
        grumpy_customers = [customers[i] * grumpy[i] for i in range(len(customers))]
        for i, n in enumerate(customers):
            cus_sum[i] = n + (cus_sum[i - 1] if i > 0 else 0)
        for i, n in enumerate(grumpy_customers):
            grum_sum[i] = n + (grum_sum[i - 1] if i > 0 else 0)
        return max((grum_sum[i - 1] if i > 0 else 0) + cus_sum[i + X - 1] - (cus_sum[i - 1] if i > 0 else 0) + grum_sum[len(customers) - 1] - grum_sum[i + X - 1] for i in range(0, len(customers) - X + 1))

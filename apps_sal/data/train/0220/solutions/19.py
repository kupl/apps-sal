class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if X == len(customers):
            return sum(customers)
        sum_not_grumpy = sum(customers[:X])
        sum_normal = sum([x * (1 - y) for x, y in zip(customers, grumpy)][X:])

        max_customers = sum_not_grumpy + sum_normal
        for i in range(1, len(customers) - X + 1):
            sum_not_grumpy -= customers[i - 1]
            sum_not_grumpy += customers[i + X - 1]
            sum_normal += customers[i - 1] * (1 - grumpy[i - 1])
            sum_normal -= customers[i + X - 1] * (1 - grumpy[i + X - 1])
            max_customers = max(max_customers, sum_not_grumpy + sum_normal)

        return max_customers

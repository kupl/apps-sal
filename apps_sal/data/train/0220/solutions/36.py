class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers:
            return 0
        can_be_always_happy = X == len(customers)
        customers_lost = [0] * (len(customers) + 1)
        total_customers_lost = 0
        total_satisfied = 0
        for idx, customer in enumerate(customers):
            if grumpy[idx] == 1 and not can_be_always_happy:
                total_customers_lost += customers[idx]
            else:
                total_satisfied += customers[idx]
            customers_lost[idx + 1] = total_customers_lost

        max_gain = 0
        for i in range(X, len(customers_lost)):
            gain = customers_lost[i] - customers_lost[i - X]
            max_gain = max(gain, max_gain)

        return total_satisfied + max_gain

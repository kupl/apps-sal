class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        tmpCustomers = customers.copy()
        totalSatisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                totalSatisfied += tmpCustomers[i]

                tmpCustomers[i] = 0

        window = 0
        best = 0

        for i in range(len(tmpCustomers)):
            window += tmpCustomers[i]
            if i >= X:
                window -= tmpCustomers[i - X]
            best = max(window, best)
        return totalSatisfied + best

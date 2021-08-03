class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfiedCustomers = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfiedCustomers += customers[i]
                customers[i] = 0
        i = 0
        unsatisfiedWindow = 0
        while i < X:
            unsatisfiedWindow += customers[i]
            i += 1

        maxUnsatisfiedWindow = unsatisfiedWindow
        while i < len(customers):
            unsatisfiedWindow -= customers[i - X]
            unsatisfiedWindow += customers[i]
            maxUnsatisfiedWindow = max(maxUnsatisfiedWindow, unsatisfiedWindow)
            i += 1

        return satisfiedCustomers + maxUnsatisfiedWindow

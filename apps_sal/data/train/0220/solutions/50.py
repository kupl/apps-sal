import numpy as np


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfiedCustomer = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                satisfiedCustomer += customers[i]
        window = 0
        for i in range(X):
            if grumpy[i] == 1:
                window += customers[i]
        res = window
        for i in range(1, len(customers) - X + 1):
            last = i - 1
            if grumpy[last] == 1:
                window -= customers[last]
            nextIdx = i + X - 1
            if grumpy[nextIdx] == 1:
                window += customers[nextIdx]
            res = max(res, window)
        return res + satisfiedCustomer

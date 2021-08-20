import numpy as np


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        customers = np.array(customers)
        grumpy = 1 - np.array(grumpy)
        l = []
        m = sum(customers * grumpy)
        for i in range(len(customers) - X + 1):
            if i == 0:
                best_case = sum(customers[0:X])
                diff = sum(grumpy[0:X] * customers[0:X])
                grump_days = best_case - diff
                l.append(grump_days)
            else:
                best_case = best_case - customers[i - 1] + customers[i + X - 1]
                diff = diff - grumpy[i - 1] * customers[i - 1] + grumpy[i + X - 1] * customers[i + X - 1]
                grump_days = best_case - diff
                l.append(grump_days)
        return max(l) + m

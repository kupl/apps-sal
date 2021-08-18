class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        s = 0

        for i in range(0, len(customers)):
            if grumpy[i] == 0:
                s += customers[i]
                customers[i] = 0

        tmp = [sum(customers[:X])]

        for i in range(X, len(customers)):

            tmp = tmp + [tmp[-1] + customers[i] - customers[i - X]]

        return max(tmp) + s

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfaction = 0
        unsatisfied = []
        for i in range(len(customers)):
            if grumpy[i] == 1:
                unsatisfied.append(customers[i])
            else:
                satisfaction += customers[i]
                unsatisfied.append(0)
        max_sum = sum(unsatisfied[:X])
        for i in range(X, len(unsatisfied) + 1):
            max_sum = max(max_sum, sum(unsatisfied[i - X:i]))
        satisfaction += max_sum
        return satisfaction

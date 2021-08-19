class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        no_tech = [0] * len(customers)
        tech = [0] * len(customers)
        if len(customers) <= X:
            return sum(customers)
        if not grumpy[0]:
            no_tech[0] = customers[0]
        tech[0] = customers[0]
        for i in range(1, len(customers)):
            if grumpy[i]:
                no_tech[i] = no_tech[i - 1]
                tech[i] = max(sum(customers[max(0, i - X + 1):i + 1]) + no_tech[i - X], tech[i - 1], no_tech[i])
            else:
                no_tech[i] = no_tech[i - 1] + customers[i]
                tech[i] = tech[i - 1] + customers[i]
        return tech[-1]

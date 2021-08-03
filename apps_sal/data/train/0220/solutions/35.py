class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # we want to find the biggest loss of satisfaction in a X-hr period throughout the day.
        if len(customers) == X:
            return sum(customers)
        maxLoss = 0
        total = sum([customers[i] * (1 - grumpy[i]) for i in range(len(grumpy))])
        print(total)
        loss = sum([grumpy[i] * customers[i] for i in range(X)])
        maxLoss = loss
        for i in range(X, len(customers)):
            loss += grumpy[i] * customers[i]
            loss -= grumpy[i - X] * customers[i - X]
            maxLoss = max(maxLoss, loss)
        total += maxLoss
        return total

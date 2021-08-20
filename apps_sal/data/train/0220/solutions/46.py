class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        initial = sum((num for (day, num) in enumerate(customers) if grumpy[day] == 0))
        curr_tricked = 0
        tricked = 0
        for (ind, num) in enumerate(customers):
            if ind >= X and grumpy[ind - X] == 1:
                curr_tricked -= customers[ind - X]
            if grumpy[ind] == 1:
                curr_tricked += customers[ind]
            tricked = max(tricked, curr_tricked)
        return initial + tricked

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sums = 0
        maxs = 0
        for i in range(len(customers)):
            sums += customers[i]
            if grumpy[i] == 1:
                grumpy[i] = customers[i]
                sums -= grumpy[i]
        for i in range(len(grumpy) - X + 1):
            maxs = max(sum(grumpy[i: i + X]), maxs)
        return sums + maxs

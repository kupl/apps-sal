class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        to_ret = sum([c for c, g in zip(customers, grumpy) if g == 0])

        mt = mf = sum([c for c, g in zip(customers[:X], grumpy[:X]) if g == 1])
        for t in range(X, len(customers)):
            if grumpy[t] == 1:
                mt += customers[t]
            if grumpy[t - X] == 1:
                mt -= customers[t - X]
            mf = max(mf, mt)
        return to_ret + mf

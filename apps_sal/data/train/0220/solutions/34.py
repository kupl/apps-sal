class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        old = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                old += customers[i]
        (l, r, res) = (0, 0, 0)
        while r < len(customers):
            if grumpy[r] == 1:
                old += customers[r]
            if r >= X:
                if grumpy[l] == 1:
                    old -= customers[l]
                l += 1
            res = max(res, old)
            r += 1
        return res

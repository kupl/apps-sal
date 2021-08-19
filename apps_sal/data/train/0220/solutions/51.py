class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = sum(c for i, c in enumerate(customers) if grumpy[i] == 0)
        add = sum(c for i, c in enumerate(customers[:X]) if grumpy[i] == 1)
        res = total + add
        #print(total, add, res)
        for i in range(X, len(customers)):
            if grumpy[i] == 1:
                add += customers[i]
            if grumpy[i - X] == 1:
                add -= customers[i - X]
            res = max(res, total + add)
            #print(total, add, res)
        return res

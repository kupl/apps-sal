class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        res = 0
        for k in range(len(customers)):
            if (grumpy[k] == 0):
                res = res + customers[k]
        diff = []
        for j in range(len(customers)):
            diff.append(customers[j] * grumpy[j])
        tem = 0
        for x in range(n - X + 1):
            tem = max(tem, sum(diff[x:x + X]))
        return res + tem

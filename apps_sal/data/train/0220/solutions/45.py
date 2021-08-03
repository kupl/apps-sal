class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(grumpy)
        if X >= n:
            return sum(customers)
        init = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])

        for j in range(X):
            if grumpy[j] == 1:
                init += customers[j]
        max_l = init
        temp = init
        for i in range(1, n - X + 1):
            temp -= grumpy[i - 1] * customers[i - 1]
            temp += grumpy[i + X - 1] * customers[i + X - 1]
            max_l = max(max_l, temp)

        return max_l

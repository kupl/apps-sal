class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = 0
        L = len(grumpy)
        if X >= L:
            return sum(customers)
        for i in range(L):
            if grumpy[i] == 0:
                ans += customers[i]
        res = cur_sum = 0
        for end in range(X):
            if grumpy[end] == 1:
                cur_sum += customers[end]
        res = cur_sum
        for end in range(X, L):
            if grumpy[end] == 1:
                cur_sum += customers[end]
            if grumpy[end - X] == 1:
                cur_sum -= customers[end - X]
            res = max(res, cur_sum)
        return ans + res

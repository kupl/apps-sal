class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        start = 0
        end = X
        ans = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                ans += customers[i]
        t = 0
        for i in range(X):
            if grumpy[i] == 1:
                t += customers[i]
        maxs = 0
        while end < len(grumpy) + 1:
            if t > maxs:
                maxs = t
            if end == len(grumpy):
                break
            if grumpy[start] == 1:
                t -= customers[start]
            if grumpy[end] == 1:
                t += customers[end]
            start += 1
            end += 1
        return ans + maxs

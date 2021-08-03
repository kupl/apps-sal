class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = 0

        for i in range(len(customers)):
            total += (1 - grumpy[i]) * customers[i]
            grumpy[i] *= customers[i]

        maxsum = 0
        for i in range(X):
            maxsum += grumpy[i]
        cur = maxsum
        for j in range(X, len(grumpy)):
            i = j - X
            cur += grumpy[j]
            cur -= grumpy[i]
            maxsum = max(maxsum, cur)
        # print(maxsum)
        return total + maxsum

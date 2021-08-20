class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        curr = 0
        max1 = 0
        left = 0
        for i in range(len(customers)):
            if i < X:
                curr += customers[i]
            elif grumpy[i] == 0:
                curr += customers[i]
        max1 = curr
        for i in range(X, len(customers)):
            if grumpy[i] == 1:
                curr += customers[i]
            if grumpy[left] == 1:
                curr -= customers[left]
            left += 1
            max1 = max(max1, curr)
        return max1

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        gc = []
        l = len(customers)
        for i in range(l):
            gc.append(customers[i] * grumpy[i])

        ms = 0
        mi = -1
        for i in range(l - X + 1):
            s = sum(gc[i:i + X])
            if s > ms:
                ms = s
                mi = i
        allowed = range(mi, mi + X)
        ans = 0
        for i in range(l):
            if grumpy[i] == 0 or i in allowed:
                ans += customers[i]

        return ans

class Solution:

    def maxCoins(self, a):
        a.sort()
        n = len(a)
        return sum((a[i] for i in range(n // 3, n, 2)))

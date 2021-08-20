class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        (a, b) = (1, 1)
        while b <= k:
            (a, b) = (b, a + b)
        res = 0
        while a > 0:
            if k >= a:
                k -= a
                res += 1
            (a, b) = (b - a, a)
        return res

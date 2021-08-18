class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        if k == 0:
            return 0

        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1

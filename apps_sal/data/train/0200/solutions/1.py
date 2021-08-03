class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = b = 1
        fibo = [a, b]

        res = 0
        while a + b <= k:
            fibo.append(a + b)
            a, b = b, a + b
        for i in fibo[::-1]:
            if k >= i:
                k -= i
                res += 1
        return res

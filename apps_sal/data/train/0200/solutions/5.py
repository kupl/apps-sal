class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k
        f1, f2 = 1, 1
        while f2 <= k:
            f1, f2 = f2, f1 + f2
        t = 0
        while k:
            # print(f1, f2, k, t)
            if f2 <= k:
                k -= f2
                t += 1
            else:
                f1, f2 = f2 - f1, f1
        return t

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        digits = list(map(int, str(N)))
        n = len(digits)
        d = 0
        for i in range(1, n):
            d += 9 * math.factorial(9) // math.factorial(10 - i)
        for i, j in enumerate(digits):
            for k in range(1 if i == 0 else 0, j):
                if k in digits[:i]:
                    continue
                x = 10 - i - 1
                d += math.factorial(x) // math.factorial(x - (n - i - 1))
            if j in digits[:i]:
                break
            else:
                if i == n - 1:
                    d += 1
        return N - d

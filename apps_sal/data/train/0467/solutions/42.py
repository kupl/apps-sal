class Solution:
    def divs(self, x):
        L = 2 if x > 1 else 1
        S = (1 + x) if x > 1 else 1
        for a in range(2, x):
            if (a**2) > x:
                break
            if not x % a:
                L += 1 if x == (a**2) else 2
                S += a if x == (a**2) else (a + x // a)
            if L > 4:
                break
        return L, S

    def sumFourDivisors(self, A):
        self.memo = {}
        res = 0
        for x in A:
            L, S = self.divs(x)
            if L == 4:
                res += S
        return res

class Solution:
    def power(self, n):
        c = 0
        while n != 1:
            if n % 2:
                n = (n * 3) + 1
            else:
                n //= 2
            c += 1
        return c

    def getKth(self, lo: int, hi: int, k: int) -> int:
        e = [i for i in range(lo, hi + 1)]
        e.sort(key=self.power)
        return e[k - 1]

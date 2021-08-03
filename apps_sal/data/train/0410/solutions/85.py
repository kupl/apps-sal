class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(n):
            step = 0
            while n != 1:
                n = 3 * n + 1 if n % 2 else n / 2
                step += 1
            return step
        powers = sorted([(i, getPower(i)) for i in range(lo, hi + 1)], key=lambda x: (x[1], x[0]))
        return powers[k - 1][0]

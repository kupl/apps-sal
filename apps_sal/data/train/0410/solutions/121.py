class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(n):
            if n == 1:
                return 0
            return (getPower(3 * n + 1) if n % 2 else getPower(n / 2)) + 1
        powers = sorted([(i, getPower(i)) for i in range(lo, hi + 1)], key=lambda x: (x[1], x[0]))
        return powers[k - 1][0]

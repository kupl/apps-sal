class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getPower(n):
            return 0 if n == 1 else (getPower(3 * n + 1) if n % 2 else getPower(n / 2)) + 1
        return sorted(range(lo, hi + 1), key=getPower)[k - 1]

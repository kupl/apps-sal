class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getF(x):
            if x == 1:
                return 0
            return getF(3 * x + 1) + 1 if x % 2 == 1 else getF(x // 2) + 1
        weights = list(range(lo, hi + 1))
        weights = sorted(weights, key=lambda x: getF(x))
        return weights[k - 1]

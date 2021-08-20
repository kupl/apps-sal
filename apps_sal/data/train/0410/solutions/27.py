class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def power(x):
            res = 0
            while x != 1:
                if x % 2 == 0:
                    x = x >> 1
                else:
                    x = x * 3 + 1
                res += 1
            return res
        x = sorted([i for i in range(lo, hi + 1)], key=power)
        return x[k - 1]

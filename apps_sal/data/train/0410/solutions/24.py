class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            r = 0
            while x > 1:
                if x % 2 == 0:
                    # x /= 2
                    x >>= 1
                else:
                    x = 3 * x + 1
                r += 1
            return r

        array = (i for i in range(lo, hi + 1))
        array = sorted(array, key=lambda x: power(x))

        return array[k - 1]

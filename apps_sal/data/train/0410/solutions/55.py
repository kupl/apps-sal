class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(map(lambda x: (self.myfunc(x), x), range(lo, hi + 1)))[k - 1][1]

    def myfunc(self, x):
        transformations = 0
        while x != 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            transformations += 1
        return transformations

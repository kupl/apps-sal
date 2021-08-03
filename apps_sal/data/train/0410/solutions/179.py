from collections import defaultdict


class Solution:
    def helper(self, x):
        if x == 2:
            return 1
        if x in self.table:
            return self.table[x]
        if x % 2:
            y = int(3 * x + 1)
        else:
            y = int(x / 2)
        ans = 1 + self.helper(y)
        self.table[x] = ans
        return ans

    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.table = dict()
        self.lo = lo
        self.hi = hi
        powers = [self.helper(x) for x in range(lo, hi + 1)]
        tosort = list(zip(powers, list(range(lo, hi + 1))))
        return sorted(tosort)[k - 1][1]
        # print(ranks)

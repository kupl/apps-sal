class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo, hi + 1):
            count = 0
            j = i
            while j > 1:
                if j & 1:
                    j = 3 * j + 1
                else:
                    j //= 2
                count += 1
            res.append((count, i))
        res.sort()
        return res[k - 1][1]

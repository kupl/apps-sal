class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def transform(v):
            times = 0
            while v != 1:
                times += 1
                if v % 2 == 0:
                    v = v / 2
                else:
                    v = 3 * v + 1
            return times
        res = []
        for x in range(lo, hi + 1):
            power = transform(x)
            res.append([power, x])
        res.sort(key=lambda x: (x[0], x[1]))
        return res[k - 1][1]

class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for num in range(lo, hi + 1):
            var = num
            count = 0
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                count += 1
            res.append([count, var])
        res.sort()
        return res[k - 1][1]

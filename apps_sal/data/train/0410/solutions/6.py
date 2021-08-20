class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for num in range(lo, hi + 1):
            steps = 0
            tmp = num
            while num > 1:
                if num % 2:
                    num = 3 * num + 1
                else:
                    num //= 2
                steps += 1
            res.append((steps, tmp))
        res.sort()
        return res[k - 1][1]

class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        dic = {}
        for num in range(lo, hi + 1):
            if num in dic:
                res.append((dic[num], num))
                continue
            (steps, tmp) = (0, num)
            while num > 1:
                if num in dic:
                    steps += dic[num]
                    break
                if num % 2:
                    num = 3 * num + 1
                else:
                    num //= 2
                steps += 1
            dic[tmp] = steps
            res.append((steps, tmp))
        res.sort()
        return res[k - 1][1]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def powerx(x):
            p = 0
            while x != 1:
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = x * 3 + 1
                p += 1
            return p
        dic = {}
        for i in range(lo, hi + 1):
            dic[i] = powerx(i)
        dic_ordered = sorted(list(dic.items()), key=lambda x: x[1])
        return(dic_ordered[k - 1][0])

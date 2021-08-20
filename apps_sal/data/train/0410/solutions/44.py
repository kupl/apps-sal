class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        dict1 = {}
        for i in range(lo, hi + 1, 1):
            c = 0
            r = []
            v = 0
            p = i
            while c == 0:
                if i == 1:
                    c = 1
                elif i % 2 == 0:
                    i = i // 2
                    v += 1
                    while i % 2 == 0:
                        i = i // 2
                        v += 1
                else:
                    i = i * 3 + 1
                    v += 1
            r.append(p)
            r.append(v)
            res.append(r)
        res.sort(key=lambda x: x[1])
        print(res)
        return res[k - 1][0]

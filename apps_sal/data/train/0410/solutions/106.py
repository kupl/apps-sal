class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        x = {}
        for i in range(lo, hi + 1):
            j = []
            g = i
            while i != 1:
                if i % 2 == 0:
                    i = i / 2
                    j.append(i)
                else:
                    i = 3 * i + 1
                    j.append(i)
            x[g] = len(j)
        x = sorted(x, key=x.get)
        return x[k - 1]

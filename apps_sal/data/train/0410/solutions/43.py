from operator import itemgetter
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        z = []
        for i in range(lo, hi + 1):
            count = 0
            f=i
            while i != 1:
                if i % 2 == 0:
                    i = i / 2
                    count += 1
                else:
                    i = 3 * i + 1
                    count += 1
            z.append([f, count])
        return sorted(z, key=itemgetter(1))[k-1][0]

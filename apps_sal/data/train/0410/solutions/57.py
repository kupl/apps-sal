class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        low = lo
        high = hi
        countlist = []
        intgererlist = []
        for lo in range(low, high + 1):
            i = lo
            count = 0
            while lo > 1:
                if lo % 2 == 0:
                    lo = lo // 2
                else:
                    lo = 3 * lo + 1
                count += 1
            countlist.append(count)
            intgererlist.append(i)
        ziped = zip(countlist, intgererlist)
        o = 0
        for (i, j) in sorted(ziped):
            o += 1
            if o == k:
                return j

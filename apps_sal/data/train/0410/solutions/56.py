class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        indexList = [i for i in range(lo, hi + 1, 1)]
        powerList = [self.getPower(i) for i in indexList]
        sortedIndex = [x for (_, x) in sorted(zip(powerList, indexList))]
        return sortedIndex[k - 1]

    def getPower(self, x: int) -> int:
        count = 0
        while x != 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            count += 1
        return count

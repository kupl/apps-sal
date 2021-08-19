class Solution:

    def getPowVal(self, x: int) -> int:
        if x in self.memo:
            return self.memo[x]
        newX = x // 2 if x % 2 == 0 else 3 * x + 1
        self.memo[x] = 1 + self.getPowVal(newX)
        return self.memo[x]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {1: 0}
        powVal = [(x, self.getPowVal(x)) for x in range(lo, hi + 1)]
        powVal.sort(key=lambda x: x[1])
        return powVal[k - 1][0]

class Solution:
    def findPower(self, ele):
        ctr = 0
        while ele != 1:
            if ele % 2 == 0:
                ele = ele // 2
            else:
                ele = 3 * ele + 1
            ctr += 1
        return ctr

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powmat = []
        for i in range(lo, hi + 1):
            ct = self.findPower(i)
            powmat.append([ct, i])
        powmat.sort()
        print(powmat)
        return powmat[k - 1][1]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        self.dic = {1: 0}
        for i in range(lo, hi + 1):
            c = self.solvePower(i)
            ans.append([c, i])

        ans.sort()
        return ans[k - 1][1]

    def solvePower(self, num):
        if self.dic.get(num, None) != None:
            return self.dic[num]

        if num % 2 == 0:
            temp = self.solvePower(num // 2)
        else:
            temp = self.solvePower(num * 3 + 1)

        self.dic[num] = 1 + temp
        return self.dic[num]

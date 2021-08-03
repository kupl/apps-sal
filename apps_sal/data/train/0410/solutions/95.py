class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo, hi + 1):
            power = self.findPower(i, 0)
            dic[i] = power
        sortedValue = sorted(list(dic.items()), key=lambda x: x[1])
        return (sortedValue[k - 1][0])

    def findPower(self, num, count):
        if num == 1:
            return count
        elif num % 2 == 0:
            return self.findPower(num // 2, count + 1)
        else:
            return self.findPower(3 * num + 1, count + 1)

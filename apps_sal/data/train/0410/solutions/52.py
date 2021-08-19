class Solution:
    powers = {1: 0}

    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_range = []
        for i in range(lo, hi + 1):
            tup = (i, self.getPower(i))
            power_range.append(tup)
        power_range.sort(key=lambda x: x[1])
        return power_range[k - 1][0]

    def getPower(self, num):
        if num in self.powers:
            return self.powers[num]
        if num % 2 == 1:
            power = self.getPower(num * 3 + 1) + 1
            self.powers[num] = power
            return power
        else:
            power = self.getPower(num / 2) + 1
            self.powers[num] = power
            return power

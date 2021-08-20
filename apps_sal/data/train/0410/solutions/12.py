class Solution:

    def get_power(self, n):
        num = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            num += 1
        return num

    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {}
        for i in range(lo, hi + 1):
            power[i] = self.get_power(i)
        return sorted(list(power.keys()), key=lambda x: power[x])[k - 1]

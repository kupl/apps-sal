class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {}
        for x in range(lo, hi + 1):
            power[x] = self._get_power(x, power)
        return sorted(power, key=power.get)[k - 1]

    def _get_power(self, x, power):
        if x in power:
            return power[x]
        if x == 1:
            return 0
        if x % 2 == 0:
            return self._get_power(x // 2, power) + 1
        else:
            return self._get_power(3 * x + 1, power) + 1

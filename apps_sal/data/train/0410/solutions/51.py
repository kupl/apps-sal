class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_values = defaultdict()
        for i in range(lo, hi + 1):
            count = 0
            x = i
            while x != 1:
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3 * x + 1
                count += 1
            power_values[i] = count
        sorted_d = sorted(power_values.items(), key=lambda x: x[1])
        return sorted_d[k - 1][0]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def find_power_value(n: int, steps: int) -> int:
            if n == 2: return steps + 1
            if n % 2 == 0:
                return find_power_value(n // 2, steps + 1)
            return find_power_value(3 * n + 1, steps + 1)
        result = [ ]
        for i in range(lo, hi + 1):
            result.append((find_power_value(i, 0), i))
        result.sort()
        return result[k - 1][1]


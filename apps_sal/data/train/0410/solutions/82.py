class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + power(x // 2)
            return 1 + power(3 * x + 1)

        return sorted(range(lo, hi + 1), key=power)[k - 1]

        len_powers = [0] * (hi - lo + 1)
        for n in range(lo, hi + 1):
            ls_power = [n]
            while ls_power[-1] != 1:
                if ls_power[-1] % 2 == 0:
                    ls_power.append(ls_power[-1] // 2)
                else:
                    ls_power.append(3 * ls_power[-1] + 1)
            len_powers[n - lo] = len(ls_power) - 1
        return sorted(zip(range(lo, hi + 1), len_powers), key=lambda x: [x[1], x[0]])[k - 1][0]

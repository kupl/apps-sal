class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0

        f = [None] * (target + 1)

        f[0] = 0

        for i in range(1, target + 1):
            f[i] = float('inf')

            k = i.bit_length()

            if i == 2 ** k - 1:
                f[i] = k
                continue

            for j in range(k - 1):
                f[i] = min(f[i], f[i - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2)

            if 2 ** k - 1 - i < i:
                f[i] = min(f[i], f[2 ** k - 1 - i] + k + 1)
        return f[target]

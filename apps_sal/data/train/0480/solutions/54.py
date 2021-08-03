class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        real_len = min(steps, arrLen) + 2
        f1 = [0 for _ in range(real_len)]
        f1[0] = 1
        for _ in range(steps):
            f2 = [0 for _ in range(real_len)]
            for i in range(real_len - 1):
                for d in [-1, 0, 1]:
                    ii = i + d
                    if ii >= 0 and ii <= arrLen - 1:
                        f2[i] += f1[ii] % mod
            f1 = f2.copy()

        return f1[0] % mod

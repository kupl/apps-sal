class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        f_old = [0] * min(steps + 1, arrLen)
        f_new = [0] * min(steps + 1, arrLen)
        if arrLen == 1:
            return 1
        elif arrLen == 0:
            return 0
        f_old[0] = 1
        for i in range(steps):
            f_new[0] = f_old[0] + f_old[1]
            if i + 1 <= arrLen - 1:
                f_new[i + 1] = 1
            else:
                f_new[-1] = f_old[-1] + f_old[-2]
            for j in range(1, min(i + 1, arrLen - 1)):
                f_new[j] = f_old[j - 1] + f_old[j] + f_old[j + 1]
            f_old = f_new.copy()
            f_old = [_ % (10 ** 9 + 7) for _ in f_old]
        return f_old[0]

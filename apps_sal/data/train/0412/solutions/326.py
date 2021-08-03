class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        if d == 1:
            return 1 if f >= target else 0

        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(i, min(i * f, target) + 1):
                # to ensure j-k >=0 means, k <=j, 至多为j,min(j, f)
                for k in range(1, min(j, f) + 1):
                    dp[i][j] += dp[i - 1][j - k]

        return dp[d][target] % (pow(10, 9) + 7)

    def __numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mem = {}
        return self.dp(d, f, target, mem) % (pow(10, 9) + 7)

    def dp(self, d, f, target, mem):
        if d == 0:
            return 1 if target == 0 else 0

        if d * f < target:
            return 0

        if (d, target) in mem:
            return mem[(d, target)]

        res = 0
        for i in range(1, f + 1):
            if target - i < 0:
                break
            res += self.dp(d - 1, f, target - i, mem)

        mem[(d, target)] = res
        return res

class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def num_rolls_util(level, target):
            if level * f < target or target < level:
                return 0
            if level == 0:
                return 1
            res = 0
            for i in range(max(0, target - f), target):
                if (level - 1, i) in memo:
                    res += memo[level - 1, i]
                else:
                    tmp = num_rolls_util(level - 1, i)
                    memo[level - 1, i] = tmp
                    res += tmp
            return res % (10 ** 9 + 7)
        return num_rolls_util(d, target)
    '\n    if target < d or target > d * f:\n            return 0\n        if target > (d*(1+f)/2):\n            target = d * (1 + f) - target\n        dp = [0] * (target + 1) \n        for i in range(1, min(f, target) + 1):\n            dp[i] = 1\n        for i in range(2, d + 1):\n            new_dp = [0] * (target + 1)\n            for j in range(i, min(target, i * f) + 1):\n                new_dp[j] = new_dp[j - 1] + dp[j - 1]\n                if j - 1 > f:\n                    new_dp[j] -= dp[j - f - 1]\n            dp = new_dp\n\n        return dp[target] % (10 ** 9 + 7)\n    '

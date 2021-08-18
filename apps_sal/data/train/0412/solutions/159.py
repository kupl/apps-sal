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
                    res += memo[(level - 1, i)]
                else:
                    tmp = num_rolls_util(level - 1, i)
                    memo[(level - 1, i)] = tmp
                    res += tmp

            return res % (10 ** 9 + 7)

        return num_rolls_util(d, target)

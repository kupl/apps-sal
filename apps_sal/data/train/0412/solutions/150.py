class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def numRollsHelper(level, target):
            if f * level < target or target < level:
                return 0

            if level == 0:
                return 1

            res = 0
            for i in range(max(target - f, 0), target):
                if (level - 1, i) in memo:
                    res += memo[(level - 1, i)]
                else:
                    tmp = numRollsHelper(level - 1, i)
                    memo[(level - 1, i)] = tmp % (10 ** 9 + 7)
                    res += tmp % (10 ** 9 + 7)

            return res

        memo = {}
        return numRollsHelper(d, target) % (10 ** 9 + 7)

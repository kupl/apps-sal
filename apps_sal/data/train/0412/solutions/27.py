class Solution:
    # Recursive memoized solution
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def num_rolls_util(level, target):
            if level == 0:
                return target == 0

            if (level, target) in memo:
                return memo[(level, target)]
            else:
                res = 0
                for i in range(max(0, target - f), target):
                    res += num_rolls_util(level - 1, i)

                memo[(level, target)] = res

                return res % (10 ** 9 + 7)
        
        return num_rolls_util(d, target)

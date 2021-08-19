class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def num_rolls_recur(d, target):
            key = (d, target)
            if key in memo:
                return memo[key]
            if target < 0:
                return 0
            if d == 0:
                if target == 0:
                    return 1
                return 0
            num_ways = 0
            for i in range(1, f + 1):
                num_ways = (num_ways + num_rolls_recur(d - 1, target - i)) % (pow(10, 9) + 7)
            memo[key] = num_ways
            return num_ways
        return num_rolls_recur(d, target)

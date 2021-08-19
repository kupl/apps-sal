class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        mod = int(math.pow(10, 9) + 7)

        def recur(d, target):
            if (d, target) in memo:
                return memo[d, target]
            if d < 0 or target < 0:
                return 0
            if d == 0 and target == 0:
                return 1
            ways = 0
            for i in range(1, f + 1):
                if target - i < 0:
                    break
                ways = int(ways + recur(d - 1, target - i)) % mod
            memo[d, target] = ways
            return ways
        return recur(d, target)

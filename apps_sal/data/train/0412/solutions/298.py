class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def dfs(dice_left, curr_sum):
            if curr_sum > target:
                return 0
            if dice_left == 0:
                return 1 if curr_sum == target else 0
            count = 0
            for i in range(1, f + 1):
                count += dfs(dice_left - 1, curr_sum + i)
            return count % 1000000007
        return dfs(d, 0)

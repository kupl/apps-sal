class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = {}
        for k in range(1, f + 1):
            dp[(1, k)] = 1

        def dfs_num_rolls(dice_left, tot_left):

            if tot_left > f**(dice_left) or tot_left < 0 or dice_left == 0:
                dp[(dice_left, tot_left)] = 0
                return 0
            if (dice_left, tot_left) in dp:
                return dp[(dice_left, tot_left)]

            total = 0
            for k in range(1, f + 1):
                total += dfs_num_rolls(dice_left - 1, tot_left - k) % (10**9 + 7)

            total = total % (10**9 + 7)
            dp[(dice_left, tot_left)] = total
            return total

        dfs_num_rolls(d, target)
        return dp[(d, target)]

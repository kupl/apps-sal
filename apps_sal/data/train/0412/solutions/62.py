class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        def count_for_roll(num_dice, curr_target):
            if num_dice == 0 and curr_target == 0:
                return 1
            if num_dice == 0 or curr_target == 0:
                return 0
            if (num_dice, curr_target) in memo:
                return memo[num_dice, curr_target]
            curr_count = 0
            for face in range(1, f + 1):
                new_target = curr_target - face
                if new_target < 0:
                    break
                curr_count += count_for_roll(num_dice - 1, new_target)
            memo[num_dice, curr_target] = curr_count
            return curr_count % mod
        memo = {}
        mod = 10 ** 9 + 7
        return count_for_roll(d, target)


'\nd = 2, f = 6, t = 7\n\n1\n    1\n    2\n    3\n    4\n    5\n    6 -> inc\n    \n2\n    1\n    2\n    3\n    4\n    5 -> inc\n    6 -> stop?\n    \n3 \n    1\n    2\n    3\n    4 -> inc\n    5 -> stop\n    \n    \n\n'

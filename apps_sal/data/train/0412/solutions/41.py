class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def find_next(dice_left, current_val):
            if current_val > target:
                return 0
            if dice_left == 0:
                if current_val == target:
                    return 1
                return 0

            if (dice_left, current_val) not in seen:
                combinations = 0
                for i in range(1, f + 1):
                    combinations += find_next(dice_left - 1, current_val + i)
                seen[(dice_left, current_val)] = combinations % 1000000007

            return seen[(dice_left, current_val)]

        seen = {}
        return find_next(d, 0)

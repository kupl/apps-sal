import numpy as np


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Choose m values from n such that the minimum of the differences is maximized
        position.sort()

        def check(check_val):
            temp_m = m - 1

            previous_pos = position[0]

            for p in position[1:]:
                if p - previous_pos >= check_val:
                    previous_pos = p
                    temp_m -= 1
                    if temp_m == 0:
                        return True
            return False

        l = 0   # min return value
        r = (position[-1] - position[0]) // (m - 1) + 1  # max return value

        ret = l
        while l <= r:
            val = (l + r) // 2
            if check(val):
                ret = max(ret, val)
                l = val + 1
            else:
                r = val - 1
        return ret

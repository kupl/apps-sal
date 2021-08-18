import numpy as np


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
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

        l = 0
        r = (position[-1] - position[0]) // (m - 1) + 1

        ret = l
        while l <= r:
            val = (l + r) // 2
            if check(val):
                ret = max(ret, val)
                l = val + 1
            else:
                r = val - 1
        return ret

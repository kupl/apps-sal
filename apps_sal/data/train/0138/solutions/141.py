from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        left_size = []
        left_mult = []

        size = 0
        mult = 0

        for val in nums:
            if val == 0:
                size = 0
                mult = 0
            else:
                size += 1
                mult += (1 if val < 0 else 0)

            left_size.append(size)
            left_mult.append(mult)

        right_size = []
        right_mult = []

        size = 0
        mult = 0

        for val in nums[::-1]:
            if val == 0:
                size = 0
                mult = 0
            else:
                size += 1
                mult += (1 if val < 0 else 0)

            right_size.append(size)
            right_mult.append(mult)

        right_size = right_size[::-1]
        right_mult = right_mult[::-1]

        ans = 0
        for idx, val in enumerate(nums):
            if val == 0:
                continue

            ls = 0
            lm = 0
            if idx > 0:
                ls = left_size[idx - 1]
                lm = left_mult[idx - 1]

            rs = 0
            rm = 0
            if idx < len(nums) - 1:
                rs = right_size[idx + 1]
                rm = right_mult[idx + 1]

            cur = int(val < 0)

            if lm % 2 == 0:
                ans = max(ans, ls)
            if val > 0:
                ans = max(ans, 1)
            if (lm + cur) % 2 == 0:
                ans = max(ans, ls + 1)
            if rm % 2 == 0:
                ans = max(ans, rs)
            if (rm + cur) % 2 == 0:
                ans = max(ans, rs + 1)
            if (lm + cur + rm) % 2 == 0:
                ans = max(ans, ls + rs + 1)

        return ans

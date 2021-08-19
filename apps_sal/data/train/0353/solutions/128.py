from collections import Counter


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        c = Counter(nums)
        nums = []
        for (k, v) in sorted(list(c.items()), key=lambda x: x[0]):
            nums.extend([k] * v)
        res = 0
        (i1, i2) = (0, len(nums) - 1)
        while i1 <= i2:
            if nums[i1] + nums[i2] <= target:
                res += 2 ** (i2 - i1)
                i1 += 1
            else:
                i2 -= 1
        return res % (10 ** 9 + 7)

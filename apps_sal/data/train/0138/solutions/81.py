class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ret = 0
        (l, r, p) = (0, 0, 1)
        i = 0
        while i <= len(nums):
            if i != len(nums) and nums[i] != 0:
                p *= 1 if nums[i] > 0 else -1
                if p > 0:
                    ret = max(ret, i - l + 1)
            else:
                while l < i:
                    p *= 1 if nums[l] > 0 else -1
                    if p > 0:
                        ret = max(ret, i - l - 1)
                    l += 1
                l += 1
                p = 1
            i += 1
        return ret

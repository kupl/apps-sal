class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx, mi = [0], [0]
        res = 1
        left = 0
        for c in range(1, len(nums)):
            num = nums[c]
            while mx and nums[mx[-1]] < num:
                mx.pop()
            mx.append(c)
            while mi and nums[mi[-1]] > num:
                mi.pop()
            mi.append(c)
            while mi and mx and nums[mx[0]] - nums[mi[0]] > limit:
                left += 1
                if left > mx[0]:
                    mx.pop(0)
                if left > mi[0]:
                    mi.pop(0)
            res = max(res, c - left + 1)
        return res

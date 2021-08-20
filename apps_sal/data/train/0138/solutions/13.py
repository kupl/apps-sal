class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pre_pos = pos
                pos = 1 + neg if neg > 0 else 0
                neg = 1 + pre_pos
            else:
                (pos, neg) = (0, 0)
            ans = max(ans, pos)
        return ans

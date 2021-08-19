class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (pos, neg) = (0, 0)
        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                (pos, neg) = (pos + 1, neg + 1 if neg else 0)
            elif nums[i] < 0:
                (pos, neg) = (neg + 1 if neg else 0, pos + 1)
            else:
                (pos, neg) = (0, 0)
            ans = max(ans, pos)
        return ans

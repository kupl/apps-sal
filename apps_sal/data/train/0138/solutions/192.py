class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        (pos, neg) = (0, 0)
        for i in range(len(nums)):
            if nums[i] > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:
                (pos, neg) = (neg + 1 if neg > 0 else 0, pos + 1)
            else:
                (pos, neg) = (0, 0)
            ans = max(ans, pos)
        return ans

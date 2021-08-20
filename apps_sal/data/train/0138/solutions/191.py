class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        f = [0, 0]
        ans = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                f = [f[1] + 1 if f[1] > 0 else 0, f[0] + 1]
            elif nums[i] > 0:
                f = [f[0] + 1, f[1] + 1 if f[1] > 0 else 0]
            else:
                f = [0, 0]
            ans = max(ans, f[0])
        return ans

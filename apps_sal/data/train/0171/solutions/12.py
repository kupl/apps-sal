class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [[nums[0], nums[0]]]
        ans = nums[0]
        for i in range(1, len(nums)):
            f.append([0, 0])
            f[i][0] = min(f[i - 1][0] * nums[i], f[i - 1][1] * nums[i], nums[i])
            f[i][1] = max(f[i - 1][0] * nums[i], f[i - 1][1] * nums[i], nums[i])
            ans = max(ans, f[i][1])
        return ans

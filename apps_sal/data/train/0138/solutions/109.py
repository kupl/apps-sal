class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp_f = [-1] * (n + 1)
        dp_g = [-1] * (n + 1)

        dp_f[0] = 0
        dp_g[0] = 0

        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dp_f[i] = 0
                dp_g[i] = 0
            elif nums[i - 1] > 0:
                dp_f[i] = dp_f[i - 1] + 1
                dp_g[i] = dp_g[i - 1] + 1 if dp_g[i - 1] > 0 else 0
            else:
                dp_f[i] = dp_g[i - 1] + 1 if dp_g[i - 1] > 0 else 0
                dp_g[i] = dp_f[i - 1] + 1
        return max(dp_f)

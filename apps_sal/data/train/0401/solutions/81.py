class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [[0] * 3 for i in range(len(nums))]
        f[0][nums[0] % 3] = nums[0]
        for i in range(1, len(nums)):
            for j in range(3):
                include = f[i - 1][(j - nums[i]) % 3] + nums[i]
                if include % 3 == j:
                    f[i][j] = max(f[i - 1][j], include)
                else:
                    f[i][j] = f[i - 1][j]
        return f[-1][0]

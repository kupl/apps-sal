class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        f = [[0, 0] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] < 0:
                f[i + 1] = [f[i][1] + 1 if f[i][1] > 0 else 0, f[i][0] + 1]
            elif nums[i] > 0:
                f[i + 1] = [f[i][0] + 1, f[i][1] + 1 if f[i][1] > 0 else 0]
        # print(f)
        return max(x[0] for x in f)

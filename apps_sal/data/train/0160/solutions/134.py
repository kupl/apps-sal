class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n, f = len(nums), [i for i in nums]
        for i in range(1, n):
            for j in range(n - i):
                f[j] = max(nums[j] - f[j + 1], nums[j + i] - f[j])
        return f[0] > 0

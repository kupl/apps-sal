class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        grid = [[0] * len(nums) for x in range(len(nums))]
        res = []
        for i in range(len(nums)):
            grid[i][i] = nums[i]
            res.append(grid[i][i])
        for j in range(len(nums)):
            for i in range(j - 1, -1, -1):
                grid[i][j] = grid[i + 1][j] + nums[i]
                res.append(grid[i][j])
        res.sort()
        return sum(res[left - 1:right]) % (10**9 + 7)

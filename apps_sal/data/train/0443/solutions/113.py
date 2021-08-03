class Solution:
    def numTeams(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([1 if (nums[i] < nums[j] and nums[j] < nums[k]) or (nums[i] > nums[j] and nums[j] > nums[k]) else 0 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n)])

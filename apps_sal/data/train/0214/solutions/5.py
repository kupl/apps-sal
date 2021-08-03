class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res = [0, 0]

        for i in range(len(nums)):
            res[i % 2] += max(nums[i] + 1 - min(nums[i - 1] if i else float('inf'), nums[i + 1] if i < len(nums) - 1 else float('inf')), 0)

        return min(res)

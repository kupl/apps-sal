class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        print(nums)
        cur = max(nums) - min(nums)

        h1 = nums[0]
        nums[0] = nums[-1]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0] = h1

        h1, h2 = nums[0], nums[1]
        nums[0], nums[1] = nums[-1], nums[-1]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[1] = h1, h2

        h1, h2, h3 = nums[0], nums[1], nums[2]
        nums[0], nums[1], nums[2] = nums[-1], nums[-1], nums[-1]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[1], nums[2] = h1, h2, h3

        h1, h2, h3 = nums[-1], nums[-2], nums[-3]
        nums[-1], nums[-2], nums[-3] = nums[0], nums[0], nums[0]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[-1], nums[-2], nums[-3] = h1, h2, h3

        h1, h2 = nums[-1], nums[-2]
        nums[-1], nums[-2] = nums[0], nums[1]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[-1], nums[-2] = h1, h2

        h1 = nums[-1]
        nums[-1] = nums[0]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[-1] = h1

        h1, h2, h3 = nums[0], nums[1], nums[-1]
        nums[0], nums[1], nums[-1] = nums[2], nums[2], nums[2]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[1], nums[-1] = nums[-2], nums[-2], nums[-2]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[1], nums[-1] = h1, h2, h3

        h1, h2, h3 = nums[0], nums[-1], nums[-2]
        nums[0], nums[-1], nums[-2] = nums[1], nums[1], nums[1]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[-1], nums[-2] = nums[-3], nums[-3], nums[-3]
        if max(nums) - min(nums) < cur:
            cur = max(nums) - min(nums)
        nums[0], nums[-1], nums[-2] = h1, h2, h3

        return cur

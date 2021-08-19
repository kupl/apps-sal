class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        even = odd = 0
        n = len(nums)
        for i in range(n):
            prev = nums[i - 1] if i - 1 >= 0 else float('inf')
            next = nums[i + 1] if i + 1 < n else float('inf')
            change = max(0, nums[i] - min(prev, next) + 1)
            if i % 2 == 0:
                even += change
            else:
                odd += change
        return min(even, odd)

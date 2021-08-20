class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        return self.sb(nums)
    '\n    걍 even 을 작게만들거나주변보다 혹은 odd를 주변보다 작게만들거나 ㅇㅇ\n    '

    def sb(self, nums):
        nums = [float('inf')] + nums + [float('inf')]
        res = [0, 0]
        for i in range(1, len(nums) - 1):
            res[i % 2] += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(res)

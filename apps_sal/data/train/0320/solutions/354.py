class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        max_zero = 0

        for i in range(len(nums)):
            zero, one = Solution.parse(nums[i])
            res += one
            max_zero = max(max_zero, zero)
        res += max_zero
        
        return res
        
    def parse(v):
        zero, one = 0, 0
        while v > 0:
            if v % 2 == 1:
                one += 1
                v -= 1
            else:
                zero += 1
                v /= 2
        return zero, one

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        a = [0] * len(nums)
        while(nums != a):
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    nums[i] = nums[i] // 2
                else:
                    op += 1
                    nums[i] -= 1
                    nums[i] = nums[i] // 2
            op += 1
        return (op - 1)

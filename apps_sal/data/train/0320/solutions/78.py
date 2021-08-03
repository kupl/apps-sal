class Solution:
    def minOperations(self, nums: List[int]) -> int:
        move = 0
        while max(nums) > 0:
            for i, num in enumerate(nums):
                if num % 2 == 1:
                    move += 1
                nums[i] = num // 2
            if max(nums) > 0:
                move += 1
        return move

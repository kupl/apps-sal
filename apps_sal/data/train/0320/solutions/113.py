class Solution:

    def minOperations(self, nums: List[int]) -> int:
        (moves, ndone) = (0, len(nums) - nums.count(0))
        while ndone:
            for (i, num) in enumerate(nums):
                if num % 2 == 1:
                    moves += 1
                    nums[i] -= 1
                    if nums[i] == 0:
                        ndone -= 1
            if ndone:
                nums = [num // 2 for num in nums]
                moves += 1
        return moves

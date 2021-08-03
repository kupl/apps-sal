class Solution:
    def minOperations(self, nums: List[int]) -> int:

        number_of_moves = 0
        while(True):
            for pos, num in enumerate(nums):
                if num % 2 == 1:
                    nums[pos] -= 1
                    number_of_moves += 1
            if not any(nums):
                break
            nums = list([x // 2 for x in nums])
            number_of_moves += 1

        return number_of_moves

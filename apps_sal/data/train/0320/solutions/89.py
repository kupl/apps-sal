class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_of_one_steps = 0
        count_of_half_steps = 0
        for i in nums:
            one_steps = 0
            half_steps = 0
            while i != 0:
                if i % 2 == 0:
                    half_steps += 1
                    i //= 2
                else:
                    one_steps += 1
                    i -= 1
            count_of_one_steps += one_steps
            count_of_half_steps = max(count_of_half_steps, half_steps)
        return count_of_one_steps + count_of_half_steps

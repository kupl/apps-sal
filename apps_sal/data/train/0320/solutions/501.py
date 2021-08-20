class Solution:

    def minOperations(self, nums: List[int]) -> int:
        highest_bit = one_bit = 0
        for i in range(32):
            for num in nums:
                if num & 1 << i:
                    highest_bit = i
                    one_bit += 1
        return highest_bit + one_bit

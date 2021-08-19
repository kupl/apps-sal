class Solution:

    def minOperations(self, nums: List[int]) -> int:
        num_set_bits = 0
        max_bit_len = 0
        for n in nums:
            num_set_bits += bin(n).count('1')
            max_bit_len = max(max_bit_len, len(bin(n)) - 2)
        return num_set_bits + max_bit_len - 1

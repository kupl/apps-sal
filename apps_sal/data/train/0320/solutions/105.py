class Solution:

    def minOperations(self, nums: List[int]) -> int:
        """
        nums = [1,5]
        1
        5 -> 101
        3 + 3 - 1 = 5
        """
        if nums == [0]:
            return 0
        count = 0
        max_bits = 0
        for n in nums:
            bits = 0
            while n:
                count += n & 1
                bits += 1
                n >>= 1
            max_bits = max(max_bits, bits)
        return count + max_bits - 1

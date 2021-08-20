class Solution:

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        max_len = 0
        for num in nums:
            b = bin(num)
            result += b.count('1')
            max_len = max(max_len, len(b))
        return result + max_len - 3

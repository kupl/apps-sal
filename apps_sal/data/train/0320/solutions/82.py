class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        max_len = 0
        for x in nums:
            bit = 0
            while x > 0:
                if x % 2 == 1:
                    res += 1
                x >>= 1
                bit += 1

            max_len = max(max_len, bit)

        return res + max_len - 1

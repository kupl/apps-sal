class Solution:

    def minOperations(self, nums):
        result = 0
        max_value = 0
        for n in nums:
            max_value = max(max_value, n)
            while n:
                if n & 1:
                    result += 1
                n = n >> 1
        if not max_value:
            return 0
        while max_value:
            result += 1
            max_value = max_value >> 1
        return result - 1

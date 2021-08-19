class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        two = 0
        for i in nums:
            mul = 0
            while i:
                if i % 2 == 1:
                    i = i - 1
                    ones += 1
                else:
                    i = i // 2
                    mul += 1
            two = max(two, mul)
        return ones + two

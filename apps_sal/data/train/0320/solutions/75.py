class Solution:
    def minOperations(self, nums: List[int]) -> int:

        multiply = 0
        add = 0

        for num in nums:
            mask = 1
            for i in range(31):
                if mask << i & num:
                    multiply = max(i, multiply)
                    add += 1

        return multiply + add

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        addOneOperations = 0 # +1 operations
        highestSetBit = 0 # *2 operations
        for bit in range(31):
            for num in nums:
                if num & (1 << bit) != 0:
                    addOneOperations += 1
                    highestSetBit = bit
        return addOneOperations + highestSetBit


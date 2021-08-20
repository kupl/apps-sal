class Solution:

    def minOperations(self, nums: List[int]) -> int:
        addOneOperations = 0
        highestSetBit = 0
        for bit in range(31):
            for num in nums:
                if num & 1 << bit != 0:
                    addOneOperations += 1
                    highestSetBit = bit
        return addOneOperations + highestSetBit

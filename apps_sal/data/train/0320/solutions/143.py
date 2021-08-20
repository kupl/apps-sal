class Solution:

    def minOperations(self, nums: List[int]) -> int:
        maxDivideCount = 0
        minusCount = 0
        for num in nums:
            divideCount = 0
            while num != 0:
                if num % 2 == 0:
                    num //= 2
                    divideCount += 1
                else:
                    num -= 1
                    minusCount += 1
            maxDivideCount = max(divideCount, maxDivideCount)
        return maxDivideCount + minusCount

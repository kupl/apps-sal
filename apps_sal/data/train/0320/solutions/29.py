class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maxTwos = 0
        totalOnes = 0
        for num in nums:
            twos, ones = self.getCount(num)
            maxTwos = max(maxTwos, twos)
            totalOnes += ones
        return totalOnes + maxTwos

    def getCount(self, num):
        twos = 0
        ones = 0
        while num > 1:
            ones += num % 2
            num //= 2
            twos += 1
        return twos, ones + num

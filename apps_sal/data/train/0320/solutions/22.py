class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maxTwos = 0
        ones = 0
        for num in nums:
            count, left = self.getCount(num)
            maxTwos = max(maxTwos, count)
            ones += left
        return ones + maxTwos

    def getCount(self, num):
        count = 0
        odd = num % 2
        if num % 2 == 1:
            num -= 1
        while num > 1:
            odd += num % 2
            num //= 2
            count += 1
        return count, num + odd

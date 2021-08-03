class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        minLength = len(nums)
        target = sum(nums) % p
        currSum = 0
        prev = {0: -1}
        for i, n in enumerate(nums):
            currSum = (currSum + n) % p
            prev[currSum] = i
            if (currSum - target) % p in prev:
                minLength = min(minLength, i - prev[(currSum - target) % p])
        if minLength < len(nums):
            return minLength
        return -1

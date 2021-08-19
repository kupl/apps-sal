class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        preSum = [i % p for i in nums]
        preSumDict = {preSum[0]: [0]}
        for i in range(1, len(nums)):
            preSum[i] = (preSum[i - 1] + nums[i]) % p
            if preSum[i] in preSumDict:
                preSumDict[preSum[i]].append(i)
            else:
                preSumDict[preSum[i]] = [i]
        if preSum[len(nums) - 1] == 0:
            return 0
        result = 10 ** 5
        for i in range(len(nums)):
            current = 0
            if i != 0:
                current = preSum[i - 1]
            gap = (current + preSum[len(nums) - 1]) % p
            if gap in preSumDict:
                for j in preSumDict[gap]:
                    if j >= i:
                        result = min(result, j - i + 1)
        if result == 10 ** 5 or result == len(nums):
            return -1
        return result

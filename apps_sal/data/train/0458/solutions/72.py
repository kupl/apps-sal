class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        lastest = {0: -1}
        total = 0
        minLeng = len(nums)
        for i in range(len(nums)):
            nums[i] %= p
            total += nums[i]
        total %= p
        if total == 0:
            return 0
        for i in range(len(nums)):
            if i > 0:
                nums[i] = (nums[i] + nums[i - 1]) % p
            x = (p - (p - nums[i] + total) % p) % p
            if lastest.get(x) is not None:
                minLeng = min(i - lastest[x], minLeng)
            lastest[nums[i]] = i
        if minLeng == len(nums):
            return -1
        return minLeng

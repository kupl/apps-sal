class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        totalRe = sum(nums) % p
        curRunningSum = 0
        posMap = collections.defaultdict(list)
        posMap[0].append(-1)
        result = float('inf')
        for i in range(len(nums)):
            curRunningSum = (curRunningSum + nums[i]) % p
            posMap[curRunningSum].append(i)
            target = (curRunningSum - totalRe) % p
            if target in posMap:
                result = min(result, i - posMap[target][-1])
        return -1 if result == len(nums) else result

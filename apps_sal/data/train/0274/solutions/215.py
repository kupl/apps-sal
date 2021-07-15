class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        thing = 0
        curMin = 9999999
        curMax = -9999999
        
        numMap = {}
        
        i = 0
        while i < len(nums):
            if nums[i] not in numMap:
                numMap[nums[i]] = 0
            numMap[nums[i]] += 1
            curMax = max(curMax, nums[i])
            curMin = min(curMin, nums[i])
            i += 1
            if curMax - curMin <= limit:
                thing = max(thing, i - l)
            else:
                p = nums[l]
                numMap[nums[l]] -= 1
                if numMap[nums[l]] == 0:
                    del numMap[nums[l]]
                l = l + 1
                if p == curMin or p == curMax:
                    curMin = min(numMap)
                    curMax = max(numMap)
        return thing

class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1
        maxL = 0
        beg = 0
        '\n        while beg<len(nums)-1:\n            #mx=max(nums[beg:(end+1)])\n            #mn=min(nums[beg:(end+1)])\n            while end<len(nums) and max(nums[beg:(end+1)])-min(nums[beg:(end+1)])<=limit:\n                maxL=max(maxL, end-beg+1)\n                end+=1\n            beg+=1\n            end=beg+1\n        return maxL\n        '
        (minQueue, maxQueue) = (collections.deque([]), collections.deque([]))
        end = beg
        while end < len(nums):
            while len(minQueue) > 0 and nums[end] < minQueue[-1]:
                minQueue.pop()
            minQueue.append(nums[end])
            while len(maxQueue) > 0 and nums[end] > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(nums[end])
            if maxQueue[0] - minQueue[0] <= limit:
                maxL = max(maxL, end - beg + 1)
            else:
                if maxQueue[0] == nums[beg]:
                    maxQueue.popleft()
                if minQueue[0] == nums[beg]:
                    minQueue.popleft()
                beg += 1
            end += 1
        return maxL

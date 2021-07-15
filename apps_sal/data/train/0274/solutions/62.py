from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        maxQ, minQ = deque(), deque()
        i = 0
        for j, val in enumerate(nums):
            while maxQ and val > maxQ[-1]: maxQ.pop()
            while minQ and val < minQ[-1]: minQ.pop()
            maxQ.append(val)
            minQ.append(val)
            if maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[i]: maxQ.popleft()
                elif minQ[0] == nums[i]: minQ.popleft()
                i += 1
        return len(nums) - i


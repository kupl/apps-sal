# 注意需要标记滑动窗口内min和max的取值， 否则有可能超时
# 这题需要使用单调栈或者最小最大堆


import heapq as hq

class Solution:
    def longestSubarray(self, nums, limit):
        mini, maxi, res, i = deque([]), deque([]), 0, 0
        for j in range(len(nums)):
            while mini and mini[-1][0] > nums[j]: mini.pop()
            mini.append((nums[j], j))
            while maxi and maxi[-1][0] < nums[j]: maxi.pop()
            maxi.append((nums[j], j))
            while abs(maxi[0][0] - mini[0][0]) > limit and i < j:
                if maxi[0][-1] <= i: maxi.popleft() 
                elif mini[0][-1] <= i: mini.popleft()
                i += 1
            res = max(res, j - i + 1)
        return res

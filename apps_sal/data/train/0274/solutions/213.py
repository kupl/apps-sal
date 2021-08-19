import collections


class minQueue(object):

    def __init__(self):
        self.queue = collections.deque()

    def append(self, val, idx):
        while self.queue and self.queue[-1][0] > val:
            self.queue.pop()
        self.queue.append((val, idx))

    def getMin(self, left_idx):
        while self.queue and self.queue[0][1] < left_idx:
            self.queue.popleft()
        return self.queue[0][0]


class maxQueue(object):

    def __init__(self):
        self.queue = collections.deque()

    def append(self, val, idx):
        while self.queue and self.queue[-1][0] < val:
            self.queue.pop()
        self.queue.append((val, idx))

    def getMax(self, left_idx):
        while self.queue and self.queue[0][1] < left_idx:
            self.queue.popleft()
        return self.queue[0][0]


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = minQueue()
        maxQ = maxQueue()
        (l, r) = (0, 0)
        minQ.append(nums[0], 0)
        maxQ.append(nums[0], 0)
        cond = True
        n = len(nums)
        res = 0
        while l <= r and r < n:
            while r < n and cond:
                res = max(res, r - l + 1)
                r += 1
                if r < n:
                    maxQ.append(nums[r], r)
                    minQ.append(nums[r], r)
                    cond = maxQ.getMax(l) - minQ.getMin(l) <= limit
            while l <= r and (not cond):
                l += 1
                cond = maxQ.getMax(l) - minQ.getMin(l) <= limit
        return res

import collections


class minQueue(object):
    def __init__(self):
        self.queue = collections.deque()

    # append val in constant time
    def append(self, val, idx):
        while self.queue and self.queue[-1][0] > val:
            self.queue.pop()
        self.queue.append((val, idx))
        # print(\"minQueue is\", self.queue)

    def getMin(self, left_idx):
        while self.queue and self.queue[0][1] < left_idx:
            self.queue.popleft()
        # print(\"l is\", left_idx, \"minQ, \",self.queue)
        return self.queue[0][0]


class maxQueue(object):
    def __init__(self):
        self.queue = collections.deque()

    # append val in constant time
    def append(self, val, idx):
        while self.queue and self.queue[-1][0] < val:
            self.queue.pop()
        self.queue.append((val, idx))
        # print(\"maxqueue is\", self.queue)

    def getMax(self, left_idx):
        while self.queue and self.queue[0][1] < left_idx:
            self.queue.popleft()
        # print(\"l is\", left_idx, \"minQ, \" ,self.queue)
        return self.queue[0][0]


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # condition is getMax - getMin <= limit
        minQ = minQueue()
        maxQ = maxQueue()
        l, r = 0, 0
        minQ.append(nums[0], 0)
        maxQ.append(nums[0], 0)
        cond = True
        n = len(nums)
        res = 0
        while l <= r and r < n:  # window meaning: l and r is included in the window
            while r < n and cond:
                # print(\"cond true l, r is\", l, r)
                res = max(res, r - l + 1)
                r += 1
                if r < n:
                    maxQ.append(nums[r], r)
                    minQ.append(nums[r], r)
                    cond = maxQ.getMax(l) - minQ.getMin(l) <= limit
            while l <= r and not cond:
                # print(\"cond false l, r is\", l, r)
                l += 1
                #print(maxQ.getMax(l), minQ.getMin(l))
                cond = maxQ.getMax(l) - minQ.getMin(l) <= limit
        return res

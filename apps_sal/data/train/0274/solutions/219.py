import heapq


class Solution:

    def __init__(self):
        self.nums = None
        self.start = None
        self.end = None
        self.q = []
        self.qmx = []

    def initialize(self):
        self.start = 0
        self.end = 0
        heapq.heappush(self.q, [self.nums[0], 0])
        heapq.heappush(self.qmx, [self.nums[0] * -1, 0])

    def moveStartRight(self):
        count = 0
        minValuePos = self.q[0][1]
        maxValuePos = self.qmx[0][1]
        self.start = min(minValuePos, maxValuePos) + 1
        while self.q[0][1] < self.start:
            heapq.heappop(self.q)
        while self.qmx[0][1] < self.start:
            heapq.heappop(self.qmx)

    def moveEndRight(self):
        self.end += 1
        if self.end < len(self.nums):
            heapq.heappush(self.q, [self.nums[self.end], self.end])
            heapq.heappush(self.qmx, [self.nums[self.end] * -1, self.end])

    def getMinMax(self):
        return (self.q[0][0], self.qmx[0][0] * -1)

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        self.nums = nums
        self.initialize()
        size = 0
        while self.end < len(self.nums):
            (minValue, maxValue) = self.getMinMax()
            if maxValue - minValue <= limit:
                size = max(size, self.end - self.start + 1)
                self.moveEndRight()
            else:
                self.moveStartRight()
        return size

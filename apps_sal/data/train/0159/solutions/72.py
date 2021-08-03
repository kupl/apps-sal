from collections import deque


class MaxQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def add(self, val, i):
        while self.queue and val > self.queue[-1][0]:
            self.queue.pop()
        self.queue.append((val, i))

        while i - self.queue[0][1] >= self.size:
            self.queue.popleft()

    def max(self):
        if self.queue:
            return self.queue[0][0]
        else:
            return 0


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = MaxQueue(k)
        result = -1
        for i in range(len(nums)):
            score = nums[i]
            prev = queue.max()
            if prev > 0:
                score += prev
            queue.add(score, i)
            result = max(result, score)
        return result

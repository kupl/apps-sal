class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        max_q = MonoQueue(False)
        min_q = MonoQueue(True)
        (l, r) = (0, 0)
        max_q.push(nums[0])
        min_q.push(nums[0])

        def in_limit():
            if max_q.is_empty() is True:
                return True
            return abs(max_q.top() - min_q.top()) <= limit
        res = 0
        while r < len(nums):
            if in_limit() is True:
                res = max(res, r - l + 1)
                r += 1
                if r < len(nums):
                    min_q.push(nums[r])
                    max_q.push(nums[r])
            else:
                min_q.popfront(nums[l])
                max_q.popfront(nums[l])
                l += 1
        return res


class MonoQueue:

    def __init__(self, inc=True):
        self.queue = []
        self.inc = inc

    def popfront(self, n):
        if self.queue[0] == n:
            self.queue.pop(0)
        return

    def push(self, n):
        while self.queue:
            if self.inc is True and self.queue[-1] > n:
                self.queue.pop(-1)
            elif self.inc is False and self.queue[-1] < n:
                self.queue.pop(-1)
            else:
                break
        self.queue.append(n)
        return

    def is_empty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0]

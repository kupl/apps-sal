from collections import deque


class MinQ:

    def __init__(self):
        self.Q = collections.deque([])

    def append(self, num):
        cnt = 0
        while self.Q and self.Q[-1][0] >= num:
            cnt += self.Q.pop()[1] + 1
        self.Q.append([num, cnt])

    def popleft(self):
        if not self.Q:
            return None
        if self.Q[0][1] == 0:
            self.Q.popleft()
        else:
            self.Q[0][1] -= 1

    @property
    def minv(self):
        return self.Q[0][0]


class MaxQ:

    def __init__(self):
        self.Q = collections.deque([])

    def append(self, num):
        cnt = 0
        while self.Q and self.Q[-1][0] <= num:
            cnt += self.Q.pop()[1] + 1
        self.Q.append([num, cnt])

    def popleft(self):
        if not self.Q:
            return None
        if self.Q[0][1] == 0:
            self.Q.popleft()
        else:
            self.Q[0][1] -= 1

    @property
    def maxv(self):
        return self.Q[0][0]


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        res = 0
        right = 0
        maxq = MaxQ()
        minq = MinQ()
        while right < n:
            maxq.append(nums[right])
            minq.append(nums[right])
            while maxq.maxv - minq.minv > limit:
                maxq.popleft()
                minq.popleft()
                left += 1
            res = max(right - left + 1, res)
            right += 1
        return res

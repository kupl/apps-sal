class MinMaxStack:

    def __init__(self):
        self.s = []
        self.mins = []
        self.maxes = []

    def append(self, x):
        self.s.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
        if not self.maxes or x >= self.maxes[-1]:
            self.maxes.append(x)

    def pop(self):
        x = self.s.pop()
        if x == self.mins[-1]:
            self.mins.pop()
        if x == self.maxes[-1]:
            self.maxes.pop()
        return x

    def min(self):
        return self.mins[-1] if self.mins else float('inf')

    def max(self):
        return self.maxes[-1] if self.maxes else -float('inf')

    def __len__(self):
        return len(self.s)


class MinMaxQueue:

    def __init__(self):
        self.s1 = MinMaxStack()
        self.s2 = MinMaxStack()

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                to_append = self.s1.pop()
                self.s2.append(to_append)
        return self.s2.pop()

    def min(self):
        return min(self.s1.min(), self.s2.min())

    def max(self):
        return max(self.s1.max(), self.s2.max())

    def __len__(self):
        return len(self.s1) + len(self.s2)


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        i = 0
        max_len = 1
        q = MinMaxQueue()
        q.enqueue(nums[0])
        while i < len(nums):
            if q.max() - q.min() <= limit:
                max_len = max(max_len, len(q))
                i += 1
                if i < len(nums):
                    q.enqueue(nums[i])
                continue
            q.dequeue()
        return max_len

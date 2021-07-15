class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        day = [0] * (n + 1)
        for i, a in enumerate(arr):
            day[a] = i + 1
        ans = -1
        max_q = MaxQueue(m)
        for i in range(1, n+1):
            max_q.pop_expired(i)
            max_q.push(day[i], i)
            if i < m:
                continue
            left = right = math.inf
            if i - m >= 1:
                left = day[i-m]
            if i + 1 <= n:
                right = day[i+1]
            if max_q.max() < (d := min(left, right)):
                ans = max(ans, d - 1)
        return ans

class MaxQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] < x:
            self.queue.pop()
        self.queue.append([x, pos])

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] >= self.size:
            self.queue.popleft()

    def max(self):
        return self.queue[0][0]

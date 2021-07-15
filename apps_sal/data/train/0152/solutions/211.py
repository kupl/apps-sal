class Solution:
    def maxDistance(self, position, m):
        position = sorted(position)
        start, end = 1, position[-1] - position[0]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check(position, m, mid):
                start = mid
            else:
                end = mid
        if self.check(position, m, end):
            return end
        if self.check(position, m, start):
            return start
    
    def check(self, position, m, delta):
        n = len(position)
        i = 1
        j = 1
        last = position[0]
        while i <= m - 1 and j <= n - 1:
            if position[j] >= last + delta:
                last = position[j]
                i += 1
            j += 1
        return i == m

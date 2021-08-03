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
        last = position[0]
        for j in range(1, n):
            if position[j] >= last + delta:
                last = position[j]
                i += 1
                if i == m:
                    return True
        return i == m

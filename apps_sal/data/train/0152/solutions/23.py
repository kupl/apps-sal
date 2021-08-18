class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            num_balls = self.count(position, m, mid)
            if num_balls > m:
                left = mid + 1
            elif num_balls == m:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def count(self, position, m, mid):
        prev = position[0]
        m = 1
        for i in position[1:]:
            if i - prev >= mid:
                m += 1
                prev = i
        return m

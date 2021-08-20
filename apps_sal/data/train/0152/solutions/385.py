class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        max_possible = (position[-1] - position[0]) // (m - 1)
        right = max_possible
        left = 0
        mid = max_possible // 2
        while left <= right:
            if self.check(position, m, mid):
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return mid

    def check(self, position, m, force):
        p = 1
        m -= 1
        prev_pos = position[0]
        while p < len(position):
            if position[p] - prev_pos >= force:
                m -= 1
                prev_pos = position[p]
            if not m:
                return True
            p += 1
        return False

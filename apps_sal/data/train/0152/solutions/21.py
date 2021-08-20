class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        max_possible_answer = (position[-1] - position[0]) // (m - 1)
        l = 1
        r = max_possible_answer + 1
        while l < r:
            mid = (r + l) // 2 + 1
            if self.is_possible(position, m, mid):
                l = mid
            else:
                r = mid - 1
        return l

    def is_possible(self, position, m, gap):
        i = 1
        prev = position[0]
        m -= 1
        while i < len(position) and m > 0:
            if position[i] - prev >= gap:
                m -= 1
                prev = position[i]
            else:
                i += 1
        return m == 0

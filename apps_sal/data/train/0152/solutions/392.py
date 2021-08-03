class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def ball_count(distance):
            prev, cnt = position[0], 1
            for pos in position[1:]:
                if pos - prev >= distance:
                    cnt += 1
                    prev = pos
            return cnt

        position.sort()
        n = len(position)
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if ball_count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

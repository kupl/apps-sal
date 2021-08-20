class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(dist):
            last_pos = position[0]
            cnt = 1
            for pos in position:
                if pos - last_pos >= dist:
                    cnt += 1
                    last_pos = pos
            return cnt
        l = 1
        r = position[-1] - position[0]
        while l < r:
            mid = (l + r + 1) // 2
            if count(mid) < m:
                r = mid - 1
            else:
                l = mid
        return l

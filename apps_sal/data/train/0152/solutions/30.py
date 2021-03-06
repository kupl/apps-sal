class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def valid(position, force):
            (prev, j) = (0, 1)
            for i in range(1, m):
                while j < len(position) and position[j] - position[prev] < force:
                    j += 1
                if j == len(position):
                    return False
                prev = j
            return True

        def getBallCount(position, force):
            (res, prev) = (1, 0)
            for i in range(1, len(position)):
                if position[i] - position[prev] >= force:
                    res += 1
                    prev = i
            return res
        position.sort()
        if m == 2:
            return position[-1] - position[0]
        (l, r, res) = (0, position[-1] + 1, 0)
        while l < r:
            mid = l + (r - l) // 2
            if getBallCount(position, mid) >= m:
                l = mid + 1
                res = mid
            else:
                r = mid
        return res

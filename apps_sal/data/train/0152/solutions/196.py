class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (1, position[-1] - position[0] + 2)
        ans = 0
        while l < r:
            mid = (l + r + 1) // 2
            (cnt, i, j) = (1, 1, 0)
            while i < len(position):
                if position[i] - position[j] >= mid:
                    cnt += 1
                    j = i
                i += 1
            if cnt >= m:
                l = mid
            else:
                r = mid - 1
        return l

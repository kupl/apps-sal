class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        (l, r, res) = (0, max(position), 0)
        position.sort()
        while l < r:
            mid = l + (r - l) // 2
            (i, cnt) = (0, 1)
            while i < len(position):
                j = i + 1
                while j < len(position):
                    if position[j] - position[i] >= mid:
                        cnt += 1
                        break
                    j += 1
                i = j
                if cnt == m:
                    break
            if cnt == m:
                l = mid + 1
                res = max(res, mid)
            else:
                r = mid
        return res

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def findcount(d):
            res = 1
            current = position[0]
            i = 1
            while i < len(position):
                if position[i] >= current + d:
                    current = position[i]
                    i += 1
                    res += 1
                else:
                    i += 1
            return res
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if findcount(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

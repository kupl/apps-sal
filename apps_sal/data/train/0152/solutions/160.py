class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def count(d):
            res = 1
            cur = position[0]
            for i in range(1, n):
                if position[i] - cur >= d:
                    res += 1
                    cur = position[i]
            return res
        n = len(position)
        position.sort()
        (l, r) = (0, position[-1] - position[0])
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

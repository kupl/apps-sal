class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def count(d):
            res = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    res += 1
                    curr = position[i]
            return res
        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = l + (r - l) // 2 + 1
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

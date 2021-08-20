class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if self.helper(mid, position) >= m:
                l = mid
            else:
                r = mid - 1
        return l

    def helper(self, d, position):
        res = 1
        cur = position[0]
        for i in range(1, len(position)):
            if position[i] - cur >= d:
                cur = position[i]
                res += 1
        return res

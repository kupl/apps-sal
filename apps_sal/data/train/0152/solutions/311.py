class Solution:

    def check(self, position, mid, m):
        prev = position[0]
        rem = m - 1
        i = 1
        while i < len(position) and rem:
            if position[i] - prev < mid:
                i += 1
            else:
                rem -= 1
                prev = position[i]
        return rem == 0

    def maxDistance(self, position: List[int], m: int) -> int:
        l = 1
        h = 1000000000
        position.sort()
        while l < h:
            mid = (l + h + 1) // 2
            if self.check(position, mid, m):
                l = mid
            else:
                h = mid - 1
        return l

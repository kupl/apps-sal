class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1]
        while l + 1 < r:
            mid = (l + r) // 2
            if self.is_ok(position, mid, m):
                l = mid
            else:
                r = mid
        if self.is_ok(position, r, m):
            return r
        return l

    def is_ok(self, position, target, m):
        count = 1
        prev = position[0]
        for i in range(1, len(position)):
            diff = position[i] - prev
            if diff >= target:
                count += 1
                prev = position[i]

        return count >= m

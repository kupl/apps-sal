class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (1, position[-1] - position[0] + 1)
        while l != r:
            mid = (l + r) // 2 + (l + r) % 2
            x = self.balls(position, mid)
            if x < m:
                r = mid - 1
            elif x >= m:
                l = mid
        return l

    def balls(self, position, d):
        ans = 1
        cur = position[0]
        for i in range(1, len(position)):
            if position[i] - cur >= d:
                cur = position[i]
                ans += 1
        return ans

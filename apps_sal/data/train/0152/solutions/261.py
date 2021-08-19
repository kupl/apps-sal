class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def isfail(mid):
            ans = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= mid:
                    ans += 1
                    curr = position[i]
            return ans < m
        left = 0
        right = max(position) - min(position) + 1
        while left < right:
            mid = (left + right) // 2
            if isfail(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1

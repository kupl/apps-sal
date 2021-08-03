class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        n = len(position)

        def countBalls(d):
            n_balls, cur = 1, position[0]

            for i in range(1, n):
                if position[i] - cur >= d:
                    n_balls += 1
                    cur = position[i]

            return n_balls

        left = 1
        right = position[n - 1] - position[0]

        while left <= right:
            mid = left + (right - left) // 2
            if countBalls(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right

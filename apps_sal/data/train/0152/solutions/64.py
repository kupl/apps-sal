class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlace(force):
            balls = 1
            curr_dist = curr_i = 0
            for i in range(1, len(position)):
                curr_dist = position[i] - position[curr_i]
                if curr_dist >= force:
                    curr_i = i
                    curr_dist = 0
                    balls += 1
            return balls
        position.sort()
        left, right = 0, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if canPlace(mid) < m:
                right = mid - 1
            else:
                left = mid
        return left

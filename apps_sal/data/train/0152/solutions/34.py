class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if len(position) < m:
            return 0

        def valid_force(f):
            ball_pos = 0
            balls = m - 1
            for i in range(1, len(position)):
                if position[i] - position[ball_pos] >= f:
                    balls -= 1
                    ball_pos = i
                    if balls == 0:
                        return True

            return False

        position.sort()
        l, h = 1, position[-1]
        while l < h:
            f = l + (h - l + 1) // 2
            if valid_force(f):
                l = f
            else:
                h = f - 1

        return l

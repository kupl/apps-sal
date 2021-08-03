class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        pos = 0
        wall = 0
        traj = 1

        while True:
            if wall == 0 and pos == p:
                return 2
            elif wall == 1 and pos == p:
                return 1
            elif wall == 1 and pos == 0:
                return 0

            if traj == 1:
                pos += q
                if pos > p:
                    pos = 2 * p - pos
                    traj *= -1
            else:
                pos -= q
                if pos < 0:
                    pos *= -1
                    traj *= -1

            wall = 1 - wall

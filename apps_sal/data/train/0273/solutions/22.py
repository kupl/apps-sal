class Solution:
    def racecar(self, target: int) -> int:
        q = [(0, 1)]
        steps = 0
        visited = set(q)
        while q:
            nxt = []
            for pos, speed in q:
                if pos + speed == target:
                    return steps + 1
                nxt_pos = pos + speed
                nxt_speed = speed * 2
                if (nxt_pos, nxt_speed) not in visited:
                    visited.add((nxt_pos, nxt_speed))
                    nxt.append((nxt_pos, nxt_speed))

                nxt_pos = pos
                nxt_speed = -1 if speed > 0 else 1
                if (nxt_pos, nxt_speed) not in visited:
                    visited.add((nxt_pos, nxt_speed))
                    nxt.append((nxt_pos, nxt_speed))
            q = nxt
            steps += 1

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
                if (pos+speed, speed*2) not in visited:
                    visited.add((pos+speed, speed*2))
                    nxt.append((pos+speed, speed*2))
                    
                nxt_speed = -1 if speed > 0 else 1
                if (pos, nxt_speed) not in visited:
                    visited.add((pos, nxt_speed))
                    nxt.append((pos, nxt_speed))
            q = nxt
            steps += 1


from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])
        visited = set([(0, 1)])
        while q:
            pos, speed, steps = q.popleft()
            if pos == target:
                return steps
            
            nxt_pos = pos + speed
            nxt_speed = speed * 2
            if (nxt_pos, nxt_speed) not in visited:
                visited.add((nxt_pos, nxt_speed))
                q.append((nxt_pos, nxt_speed, steps+1))
            
            nxt_pos = pos
            nxt_speed = -1 if speed > 0 else 1
            if (nxt_pos, nxt_speed) not in visited:
                visited.add((nxt_pos, nxt_speed))
                q.append((nxt_pos, nxt_speed, steps+1))


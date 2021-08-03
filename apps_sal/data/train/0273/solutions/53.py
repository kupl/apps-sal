from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        visited = set([(0, 1)])
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                pos, speed = q.popleft()
                if pos == target:
                    return res
                if (pos + speed, speed * 2) not in visited:
                    q.append((pos + speed, speed * 2))
                    visited.add((pos + speed, speed * 2))
                speed = 1 if speed < 0 else -1
                if (pos, speed) not in visited:
                    q.append((pos, speed))
                    visited.add((pos, speed))
            res += 1
        return res

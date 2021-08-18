from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        step = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                posi, spd = queue.popleft()
                if posi == target:
                    return step
                if ((posi + spd, 2 * spd) not in visited) and posi + spd > 0 and posi + spd < target << 1:
                    queue.append((posi + spd, 2 * spd))
                    visited.add((posi + spd, 2 * spd))
                sign = 1 if spd > 0 else -1
                if ((posi, -sign) not in visited) and posi > 0 and posi < target << 1:
                    queue.append((posi, -sign))
                    visited.add((posi, -sign))
            step += 1
        return -1

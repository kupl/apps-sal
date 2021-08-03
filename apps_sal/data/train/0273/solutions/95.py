class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set()
        visited.add((0, 1))
        step = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos + speed == target:
                    return step + 1
                if abs(speed * 2) - 1 < 2 * target and abs(pos + speed) - 2 < 2 * target:
                    queue.append((pos + speed, speed * 2))
                if speed > 0:
                    speed2 = -1
                else:
                    speed2 = 1
                if (pos, speed2) not in visited:
                    queue.append((pos, speed2))
                    visited.add((pos, speed2))
            step += 1
        return -1

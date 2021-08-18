from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        level = 0
        while True:
            size = len(queue)
            for _ in range(size):
                position, speed = queue.popleft()
                if position == target:
                    return level
                queue.append((position + speed, speed * 2))
                if position + speed > target and speed > 0 or position + speed < target and speed < 0:
                    queue.append((position, -1 if speed > 0 else 1))
            level += 1

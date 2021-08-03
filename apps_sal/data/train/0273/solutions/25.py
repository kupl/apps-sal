from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        visited = set()
        queue = deque()
        queue.append((0, 1))
        visited.add((0, 1))
        step = 1

        while queue:
            for _ in range(len(queue)):
                cur_pos, cur_speed = queue.popleft()
                next_pos, next_speed = cur_pos + cur_speed, cur_speed * 2
                if next_pos == target:
                    return step
                if (next_pos, next_speed) not in visited:
                    queue.append((next_pos, next_speed))
                    visited.add((next_pos, next_speed))
                if cur_speed > 0:
                    next_speed = -1
                else:
                    next_speed = 1
                if (cur_pos, next_speed) not in visited:
                    queue.append((cur_pos, next_speed))
                    visited.add((cur_pos, next_speed))
            step += 1

        return -1

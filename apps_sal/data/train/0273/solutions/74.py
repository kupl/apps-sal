class Solution:

    def racecar(self, target: int) -> int:
        queue = collections.deque()
        visited = set()
        queue.append((0, 1))
        visited.add((0, 1))
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                (pos, speed) = queue.popleft()
                if pos == target:
                    return steps
                next_pos = pos + speed
                if 0 < next_pos < 2 * target:
                    next_state = (next_pos, 2 * speed)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
                next_speed = -1 if speed > 0 else 1
                next_state = (pos, next_speed)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
            steps += 1
        return -1

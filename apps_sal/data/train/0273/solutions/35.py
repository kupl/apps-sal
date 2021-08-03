class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        visited = set([(0, 1)])

        step = 0
        while q:
            l = len(q)
            step += 1
            for _ in range(l):
                pos, speed = q.popleft()
                if pos == target:
                    return step - 1
                new_pos, new_speed = pos + speed, speed * 2
                if (new_pos, new_speed) not in visited:
                    q.append((new_pos, new_speed))
                    visited.add((new_pos, new_speed))

                new_pos, new_speed = pos, -1 if speed > 0 else 1
                if (new_pos, new_speed) not in visited:
                    q.append((new_pos, new_speed))
                    visited.add((new_pos, new_speed))
        return -1

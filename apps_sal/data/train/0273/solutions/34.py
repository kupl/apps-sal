class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        q.append((0, 1))
        visited = set()
        visited.add((0, 1))

        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                pos, speed = q.popleft()
                if pos == target:
                    return step

                # 'A'
                if (pos + speed, speed * 2) not in visited:
                    visited.add((pos + speed, speed * 2))
                    q.append((pos + speed, speed * 2))

                # 'R'
                if (pos > target and speed > 0) or (pos < target and speed < 0) or (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    if (pos, speed) not in visited:
                        visited.add((pos, speed))
                        q.append((pos, speed))

            step += 1

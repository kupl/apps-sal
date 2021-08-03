class Solution:
    def racecar(self, target: int) -> int:

        q = collections.deque([])
        q.append((0, 1, 0))
        visited = set()
        visited.add((0, 1))

        while q:
            pos, speed, steps = q.popleft()

            if pos == target:
                return steps

            if (pos + speed, speed * 2) not in visited:
                q.append((pos + speed, speed * 2, steps + 1))
                visited.add((pos + speed, speed * 2))

            if speed > 0:
                if (pos, -1) not in visited:
                    q.append((pos, -1, steps + 1))
                    visited.add((pos, -1))
            else:
                if (pos, 1) not in visited:
                    q.append((pos, 1, steps + 1))
                    visited.add((pos, 1))
        return -1

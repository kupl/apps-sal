class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque([(0, 1, 0)])
        visited = set()
        visited.add((0,1))

        while q:
            size = len(q)
            for _ in range(size):
                pos, speed, steps = q.popleft()
                if pos == target:
                    return steps

                cand = []
                if abs(target - (pos + speed)) < target:
                    cand.append((pos + speed, 2 * speed))
                cand.append([pos, 1 if speed < 0 else -1])
                for pos, speed in cand:
                    if (pos, speed) not in visited:
                        q.append((pos, speed, steps + 1))
                        visited.add((pos, speed))
        return -1

class Solution:
    def racecar(self, target: int) -> int:
        queue = [(0, 1)]
        step = 0
        visited = {(0, 1)}
        while queue:
            tmp = queue
            queue = []
            for pos, speed in tmp:
                if pos == target:
                    return step

                if not (pos + speed, speed * 2) in visited:
                    queue.append((pos + speed, speed * 2))
                    visited.add((pos + speed, speed * 2))
                speed = -1 if speed > 0 else 1
                if not (pos, speed) in visited:
                    queue.append((pos, speed))
                    visited.add((pos, speed))
            step += 1

        return 0

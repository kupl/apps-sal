class Solution:

    def racecar(self, target: int) -> int:
        queue = collections.deque([(1, 0)])
        visited = set(queue)
        count = 0
        while queue:
            for _ in range(len(queue)):
                (speed, pos) = queue.popleft()
                if pos < 0:
                    continue
                if pos > 2 * target:
                    continue
                if target == pos:
                    return count
                if (speed * 2, pos + speed) not in visited:
                    visited.add((speed * 2, pos + speed))
                    queue.append((speed * 2, pos + speed))
                if speed > 0:
                    if (-1, pos) not in visited:
                        visited.add((-1, pos))
                        queue.append((-1, pos))
                elif (1, pos) not in visited:
                    visited.add((1, pos))
                    queue.append((1, pos))
            count += 1
        return -1

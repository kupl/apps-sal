from collections import deque


class Solution:
    def racecar(self, target: int) -> int:

        steps = 0
        queue = deque([(0, 1)])
        cache = {(0, 1)}
        while queue:
            for _ in range(len(queue)):
                p, s = queue.popleft()
                if p == target:
                    return steps
                p1, s1 = p + s, s * 2
                p2 = p
                s2 = -1 if s > 0 else 1

                if -10000 <= p1 <= 10000 and (p1, s1) not in cache:
                    cache.add((p1, s1))
                    queue.append((p1, s1))
                if -10000 <= p2 <= 10000 and (p2, s2) not in cache:
                    cache.add((p2, s2))
                    queue.append((p2, s2))
            steps += 1

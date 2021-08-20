class Solution:

    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        level = 0
        q = deque([(0, 1)])
        visited = {(0, 1)}
        while q:
            length = len(q)
            for _ in range(length):
                (p, s) = q.popleft()
                (new_p, new_s) = (p + s, 2 * s)
                if new_p == target:
                    return level + 1
                if (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
                (new_p, new_s) = (p, -s // abs(s))
                if (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
            level += 1

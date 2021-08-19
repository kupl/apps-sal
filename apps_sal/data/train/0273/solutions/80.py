class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        # BFS solution
        level = 0
        q = deque([(0, 1)])  # tuple of (pos, speed)
        visited = {(0, 1), }
        while q:
            length = len(q)
            for _ in range(length):
                p, s = q.popleft()
                # use A
                new_p, new_s = p + s, 2 * s
                if new_p == target:
                    return level + 1
                if 0 < new_p < 2 * target and (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
                # use R
                new_p, new_s = p, -s // abs(s)
                if 0 < new_p < 2 * target and (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
            level += 1

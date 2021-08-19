from collections import deque


class Solution:

    def racecar(self, target: int) -> int:
        visited = set()
        q = deque([(0, 1, 0)])
        while q:
            (pos, sp, d) = q.popleft()
            if pos == target:
                return d
            if (pos, sp) in visited:
                continue
            visited.add((pos, sp))
            if abs(sp) > target:
                q.append((pos, -1 * (sp // abs(sp)), d + 1))
            else:
                q.append((pos + sp, sp * 2, d + 1))
                q.append((pos, -1 * (sp // abs(sp)), d + 1))

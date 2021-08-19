from collections import deque


class Solution:

    def minDays(self, n: int) -> int:
        q = deque([n])
        days = 0
        visited = set()
        while q:
            days += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == 1:
                    print(visited)
                    return days
                if node % 3 == 0 and node % 3 not in visited:
                    q.append(node // 3)
                    visited.add(node // 3)
                if node % 2 == 0 and node % 2 not in visited:
                    q.append(node // 2)
                    visited.add(node // 2)
                if node - 1 not in visited:
                    q.append(node - 1)
                    visited.add(node - 1)

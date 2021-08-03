from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        q = deque([n])
        days = 0
        visited = set()
        while q:
            days += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 1:
                    return days
                if cur % 2 == 0 and cur % 2 not in visited:
                    q.append(cur // 2)
                    visited.add(cur // 2)
                if cur % 3 == 0 and cur % 3 not in visited:
                    q.append(cur // 3)
                    visited.add(cur // 3)
                if cur - 1 not in visited:
                    q.append(cur - 1)
                    visited.add(cur - 1)

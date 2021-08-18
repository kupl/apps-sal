from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        def bfs(n, days):
            possible = -1
            q = deque([(n, 0)])
            seen = set([])
            while q:
                left, days = q.pop()

                if left == 0:
                    return days
                seen.add(left)
                if left % 2 == 0 and (left // 2 not in seen):
                    q.appendleft((left // 2, days + 1))
                if left % 3 == 0 and (left // 3 not in seen):
                    q.appendleft((left // 3, days + 1))
                if left - 1 not in seen:
                    q.appendleft((left - 1, days + 1))

        return bfs(n, 0)

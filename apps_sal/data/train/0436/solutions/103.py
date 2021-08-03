from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        visit = {}
        q = deque()
        q.append((n, 0))
        visit[n] = True
        while q:
            num_oranges, num_days = q.popleft()
            if num_oranges == 0:
                return num_days

            if not (num_oranges - 1 in visit):
                q.append((num_oranges - 1, num_days + 1))
                visit[num_oranges - 1] = True
            if num_oranges % 2 == 0 and not(num_oranges // 2 in visit):
                q.append((num_oranges // 2, num_days + 1))
                visit[num_oranges // 2] = True
            if num_oranges % 3 == 0 and not(num_oranges // 3 in visit):
                q.append((num_oranges // 3, num_days + 1))
                visit[num_oranges // 3] = True

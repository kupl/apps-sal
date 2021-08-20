class Solution:

    def minDays(self, n: int) -> int:
        queue = deque([[n, 0]])
        vis = set()
        while len(queue):
            (curr, days) = queue.popleft()
            if curr in vis:
                continue
            if curr == 0:
                return days
            vis.add(curr)
            if curr % 3 == 0:
                queue.append([curr / 3, days + 1])
            if curr % 2 == 0:
                queue.append([curr / 2, days + 1])
            queue.append([curr - 1, days + 1])

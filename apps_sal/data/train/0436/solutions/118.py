class Solution:

    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        q = collections.deque([(n, 0)])
        visited = set([n])
        while q:
            (c, step) = q.pop()
            step += 1
            if c % 3 == 0:
                nc = c // 3
                if nc == 1:
                    return step + 1
                if nc not in visited:
                    visited.add(nc)
                    q.appendleft((nc, step))
            if c % 2 == 0:
                nc = c // 2
                if nc == 1:
                    return step + 1
                if nc not in visited:
                    visited.add(nc)
                    q.appendleft((nc, step))
            if c - 1 == 1:
                return step + 1
            q.appendleft((c - 1, step))
        return -1

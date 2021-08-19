class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        (q, s) = ([], set())
        q.append((0, target))
        while q:
            (c, t) = heapq.heappop(q)
            if t == 0:
                return c - 1
            if t in s:
                continue
            s.add(t)
            n = int(log(t) / log(x))
            l = t - x ** n
            heapq.heappush(q, (c + (2 if n == 0 else n), l))
            r = x ** (n + 1) - t
            heapq.heappush(q, (c + n + 1, r))

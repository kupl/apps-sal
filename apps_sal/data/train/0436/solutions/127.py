class Solution:

    def minDays(self, n: int) -> int:
        q = deque([(n, 0)])
        seen = {n}
        while q:
            (curr, cost) = q.popleft()
            if curr == 0:
                return cost
            for nxt in [curr - 1, curr / 3, curr / 2]:
                if nxt != int(nxt):
                    continue
                nxt = int(nxt)
                if nxt in seen:
                    continue
                seen.add(nxt)
                q.append([nxt, cost + 1])

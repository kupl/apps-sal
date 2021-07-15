class Solution:
    def minDays(self, n: int) -> int:

        q = collections.deque([])
        q.append((n, 0))
        seen = set()
        while q:
            oranges, days = q.popleft()
            if oranges <= 3:
                return days + min(2, oranges)
            if oranges % 2 == 0:
                if oranges/2 not in seen:
                    q.append((oranges/2, days+1))
                    seen.add(oranges/2)
            if oranges % 3 == 0:
                if oranges-(2*(oranges/3)) not in seen:
                    q.append((oranges-(2*(oranges/3)), days+1))
                    seen.add(oranges-(2*(oranges/3)))

            if oranges-1 not in seen:
                q.append((oranges-1, days+1))
                seen.add(oranges-1)


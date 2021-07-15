class Solution:
    def minDays(self, n: int) -> int:

        q = collections.deque([])
        q.append((n, 0))
        seen = set()
        while q:
            os, days = q.popleft()
            if os == 0:
                return days
            if os % 2 == 0:
                if os/2 not in seen:
                    q.append((os/2, days+1))
                    seen.add(os/2)
            if os % 3 == 0:
                if os-(2*(os/3)) not in seen:
                    q.append((os-(2*(os/3)), days+1))
                    seen.add(os-(2*(os/3)))

            if os-1 not in seen:
                q.append((os-1, days+1))
                seen.add(os-1)
                    
        return days + 1 if not q else days


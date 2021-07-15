from collections import deque

class Solution:
    def minDays(self, n: int) -> int:
        res = 0
        if n == 0:
            return res
        q = deque([n])
        seen = set([n])
        while q:
            res += 1
            s = len(q)
            while s > 0:
                s -= 1
                i = q.popleft()
                if i % 2 == 0:
                    c = i // 2
                    if not c in seen:
                        seen.add(c)
                        q.append(c)
                if i % 3 == 0:
                    c = i // 3
                    if not c in seen:
                        seen.add(c)
                        q.append(c)
                if i - 1 == 0:
                    return res
                if not i - 1 in seen:
                    seen.add(i - 1)
                    q.append(i - 1)
        return -1     

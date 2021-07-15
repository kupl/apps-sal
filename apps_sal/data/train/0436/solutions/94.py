from collections import deque

class Solution:
    def minDays(self, n: int) -> int:
        q = deque()
        visited = set()
        q.append((n, 0))
        while len(q) > 0:
            cur, step = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            if cur == 0:
                return step
            if cur % 2 == 0:
                q.append((cur // 2, step + 1))
            if cur % 3 == 0:
                q.append((cur // 3, step + 1))
            q.append((cur - 1, step + 1))
        
        return n
        


class Solution:

    def minDays(self, n: int) -> int:
        import sys
        from collections import deque
        MAX = sys.maxsize
        mem = {}
        q = deque()
        q.append((n, 0))
        while q:
            (i, op) = q.popleft()
            if i == 0:
                return op
            if i not in mem:
                q.append((i - 1, op + 1))
                if i % 2 == 0:
                    q.append((int(i - i / 2), op + 1))
                if i % 3 == 0:
                    q.append((int(i - i / 3 * 2), op + 1))
                mem[i] = op

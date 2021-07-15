class Solution:
    def minDays(self, n: int) -> int:
        import sys
        from collections import deque
        MAX = sys.maxsize
        mem = {}
        
        q = deque()
        q.append((n,0)) # n remain, op
        
        while q:
            i, op = q.popleft()
            if i == 0:
                return op
            if i not in mem:
                # get 1
                q.append((i-1, op+1))
                # get m1 when /2
                if i % 2 == 0:
                    q.append((int(i-(i/2)), op+1))
                # get m2 when /3
                if i % 3 == 0:
                    q.append((int(i-(i/3)*2), op+1))
                mem[i] = op


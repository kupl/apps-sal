class Solution:
    def minDays(self, n: int) -> int:
        
        c = {n: 0}
        q = collections.deque([n])
        
        while 1:
            x = q.popleft()
            if x == 0: return c[x]
            if x%3 == 0 and x/3 not in c:
                c[x/3] = c[x]+1
                q.append(x/3)
            if x%2 == 0 and x/2 not in c:
                c[x/2] = c[x]+1
                q.append(x/2)
            if x-1 not in c:
                c[x-1] = c[x]+1
                q.append(x-1)

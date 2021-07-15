class Solution:
    def minDays(self, n: int) -> int:
        from collections import deque
        q = deque([(n, 1)])
        seen = set([n])
        
        while q:
            # print(q)
            node, lvl = q.popleft()
            if node==1:
                return lvl
            if node-1 not in seen:
                q.append((node-1, lvl+1))
                seen.add(node-1)
            if node%2==0 and node//2 not in seen:
                q.append((node//2, lvl+1))
                seen.add(node//2)
            if node%3==0 and node - 2*(node)//3 not in seen:
                q.append((node - 2*(node)//3, lvl+1))
                seen.add(node - 2*(node)//3)


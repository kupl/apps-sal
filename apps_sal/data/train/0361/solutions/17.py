class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        res = 0
        dq = deque([[0]*m])
        seen = {tuple([0]*m)}
        
        while dq:
            length = len(dq)
            
            for _ in range(length):
                curr = dq.popleft()
                
                minh = min(curr)
                l = curr.index(minh)
                r = l
                while r+1<m and curr[r+1]==minh:
                    r += 1
                
                for i in range(min(r-l+1, n-minh), 0, -1):
                    nxt = curr[:]
                    
                    for j in range(l, l+i):
                        nxt[j] += i
                        
                    state = tuple(nxt)
                    if state in seen:
                        continue
                    if all(j==n for j in state):
                        return res+1
                    seen.add(state)
                    dq.append(nxt)
            
            res += 1

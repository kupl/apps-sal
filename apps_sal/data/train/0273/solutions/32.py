class Solution:
    def racecar(self, target: int) -> int:
        dq = deque([(0, 1)])
        res = 0
        seen = {(0,1)}
        while dq:
            length = len(dq)
            
            for _ in range(length):
                p, s = dq.popleft()
                
                rs = -1 if s>0 else 1
                for np, ns in [[p+s, 2*s], [p, rs]]:
                    if np==target:
                        return res+1
                    
                    if (np, ns) not in seen:
                        seen.add((np, ns))
                        dq.append((np, ns))
                        
            res += 1

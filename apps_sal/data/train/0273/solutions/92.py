class Solution:
    def racecar(self, target: int) -> int:
        dq = collections.deque([(0, 1)])
        seen = set([(0,1)])
        depth = 0
        
        while True:
            k = len(dq)
            while k:
                (pos, velo) = dq.popleft()
                if pos == target:
                    return depth
                
                cand = [(pos, -1 if velo>0 else 1)]
                if abs(target- (pos+velo)) < target:
                    cand.append((pos+velo, velo*2))
                
                for (p, v) in cand:
                    if (p, v) not in seen:
                        seen.add((p,v))
                        dq.append((p,v))    
                k-=1
                
            depth+=1 
            
        
                


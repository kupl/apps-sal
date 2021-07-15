class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def method1(blocked):
            R=C=10**6
            if not (0<=source[0]<R and 0<=source[1]<C):
                return False
            
            if not (0<=target[0]<R and 0<=target[1]<C):
                return False
            
            if not blocked:
                return True
            
            blocked=set(map(tuple,blocked))
            seen=set()
            
            def neighbors(r,c):
                for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0<=nr<R and 0<=nc<C:
                        yield nr,nc
            
            def dfs(r,c):
                if (r,c) in seen:
                    return False
                
                if [r,c]==target:
                    return True
                
                if (r,c) in blocked:
                    return False
                
                seen.add((r,c))
                for nr,nc in neighbors(r,c):
                    if dfs(nr,nc):
                        return True
                return False
            
            return dfs(*source)
        
        #return method1(blocked)
    
        def method2(blocked):
            R=C=10**6
            if not (0<=source[0]<R and 0<=source[1]<C):
                return False
            
            if not (0<=target[0]<R and 0<=target[1]<C):
                return False
            
            if not blocked:
                return True
            
            blocked = set(map(tuple, blocked))
            
            def neighbors(r,c):
                for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0<=nr<R and 0<=nc<C:
                        yield nr,nc
        
            def check(source, target):
                sr, sc = source
                tr, tc = target
                level = 0
                q = collections.deque([(sr,sc)])
                vis = set()
                while q:
                    for _ in range(len(q)):
                        r,c = q.popleft()
                        if r == tr and c == tc: return True
                        for nr,nc in neighbors(r,c):
                            if (nr,nc) not in vis and (nr,nc) not in blocked:
                                vis.add((nr,nc))
                                q.append((nr,nc))
                    level += 1
                    if level == len(blocked): 
                        return True
                    
                return False
        
            return check(source, target) and check(target, source)
        
        return method2(blocked)
            
                


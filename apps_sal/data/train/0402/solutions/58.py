class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked=set(map(tuple,blocked))
       
        def dfs(x,y,target,blocked,seen):
            if not (0<=x<1e6 and 0<=y<1e6) or (x,y) in blocked or (x,y) in seen:
                return False
            seen.add((x,y))
            if len(seen)>20000 or [x,y]==target:
                return True
            return dfs(x+1,y,target,blocked,seen) or dfs(x-1,y,target,blocked,seen) or dfs(x,y+1,target,blocked,seen) or dfs(x,y-1,target,blocked,seen)
        return dfs(source[0],source[1],target,blocked,set()) and dfs(target[0],target[1],source,blocked,set())


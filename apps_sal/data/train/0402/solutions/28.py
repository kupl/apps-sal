class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int], maxNum = 10e6, bound = 200) -> bool:
        
        maxArea = bound*bound//2 + 1
        directions = [0, 1, 0, -1, 0]
        
        def dfs(x, y, t): 
            if x<0 or x>maxNum or y<0 or y>maxNum or tuple([x, y]) in block: 
                return False 
            seen.add(tuple([x, y]))
            block.add(tuple([x, y]))
            if len(seen)>maxArea or (x == t[0] and y == t[1]): 
                return True 
            for d in range(4): 
                if dfs(x+directions[d], y+directions[d+1], t): 
                    return True
            return False        
        seen = set()
        block = set(map(tuple, blocked))
        if not dfs(source[0], source[1], target): 
            return False 
        seen = set()
        block = set(map(tuple, blocked))
        return dfs(target[0], target[1], source)

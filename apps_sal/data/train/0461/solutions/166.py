class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        pass
        
        
        
        def helper(i):
            if i not in g:
                return 0
            
            children = g[i]
            nchild = len(children)
            res = 0
            for j in range(nchild):
                v = children[j]
                res = max(res,helper(v))
            return res + informTime[i]
                
                
        
        g = {}
        
        n = len(manager)
        for i in range(n):
            themanager = manager[i]
            if themanager == -1:
                continue
            if themanager not in g:
                g[themanager] = []
                
            g[themanager].append(i)
            
        return helper(headID)


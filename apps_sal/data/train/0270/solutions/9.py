class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res= []
        s='abc'
        def dfs(n, res, path):
            if n==0:
                res.append(path)
                return
            for i in s:
                if not (path and path[-1]==i):
                    dfs(n-1, res, path+i)
        dfs(n, res, '')
        res.sort()
        return res[k-1] if k<=len(res) else ''


        
        



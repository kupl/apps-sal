class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:
        res = 1

        def dfs(pos, path):
            
            nonlocal res
            if pos == len(s):
                #print(path)
                res = max(res, len(set(path)))

            for i in range(pos + 1, len(s) + 1):
                path.append(s[pos: i])
                dfs(i, path)
                path.pop()

        dfs(0, [])
        return res

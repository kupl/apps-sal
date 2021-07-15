class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i):
            nonlocal used, ret
            if i == n:
                ret = max(ret, len(used))
                return
            for j in range(i + 1, n + 1):
                w = s[i: j]
                if w in used:
                    continue
                used.add(w)
                dfs(j)
                used.discard(w)
        
        n = len(s)
        used = set()
        ret = 0
        dfs(0)
        return ret

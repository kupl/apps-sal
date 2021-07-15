class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def dfs(cur):
            if cur not in s:
                return 0
            if len(cur) == 0:
                return 0
            if cur in d:
                return d[cur]
            res = 1
            for i in range(len(cur)):
                t = cur[:i] + cur[i+1:]
                res = max(dfs(t)+1, res)
            d[cur] = res
            return d[cur]
            
        s = set(words) 
        d = {}
        _max = 0
        for w in words:
            _max = max(dfs(w), _max)
        return _max


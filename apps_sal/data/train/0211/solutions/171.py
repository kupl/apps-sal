class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #if len(set(s)) == 1: return 1
        return self.dfs(s, 0, 1, set())
    
    def dfs(self, s, start, end, dic):
        if end>=len(s): return 0 if s[start:] in dic else 1
        k1 = 0
        if s[start:end] not in dic:
            dic.add(s[start:end])
            k1 = 1+self.dfs(s, end, end+1, dic)
            dic.remove(s[start:end])
        k2 = self.dfs(s, start, end+1, dic)
        return max(k1, k2)
        


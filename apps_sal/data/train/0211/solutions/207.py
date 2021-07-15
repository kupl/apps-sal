class Solution:
    def __init__(self):    
        self.strings = []
    
    def maxUniqueSplit(self, s):
        
        n = len(s)
        result = []
        lookUp = set()
        
        self.dfs(s, lookUp, result)
        return len(self.strings)
        
    def dfs(self, s, lookUp, result):
        
        if len(s) == 0:
            if len(result) > len(self.strings):
                self.strings[:] = result
            return
        
        for i in range(0, len(s)):
            if s[0:i+1] not in lookUp:
                lookUp.add(s[0:i+1])
                result.append(s[0:i+1])
                self.dfs(s[i+1:], lookUp, result)
                lookUp.remove(s[0:i+1])
                result.pop()

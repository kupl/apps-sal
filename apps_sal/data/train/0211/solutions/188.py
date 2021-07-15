class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        maximum=0
        seen=set()
        def dfs(idx,seen):
            if idx==len(s):
                nonlocal maximum
                maximum=max(len(seen),maximum)
                return
            for i in range(idx,len(s)):
                if s[idx:i+1] not in seen:
                    seen.add(s[idx:i+1])
                    dfs(i+1,seen)
                    seen.remove(s[idx:i+1])
            
        dfs(0,seen)
        return maximum
    
                
            


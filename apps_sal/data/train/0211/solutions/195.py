class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtracking(ind):
            nonlocal ans
            if ind==len(s):
                ans = max(ans,len(split))
            
            for i in range(ind,len(s)):
                if s[ind:i+1] not in split:
                    split.add(s[ind:i+1])
                    backtracking(i+1)
                    split.remove(s[ind:i+1])
        
        ans = 0
        split = set()
        backtracking(0)
        return ans

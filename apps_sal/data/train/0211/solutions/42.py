class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        if not s:
            return 0
        self. res = 0
        stack = []
        
        def backtrack(ind):
            if ind == len(s):
                self.res = max(self.res, len(set(stack)))
            
            for i in range(ind+1, len(s)+1):
                stack.append(s[ind:i])
                backtrack(i)
                stack.pop()
        backtrack(0)
        return self.res


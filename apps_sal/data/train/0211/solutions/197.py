class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = []
        n = len(s)
        
        self.backtrack(s, 0, n, [])
                
        return len(max(self.result, key=len))
    
    
    def backtrack(self, s, left, n, currArr):
        
        if left >= n:
            self.result.append(currArr)
        
        for i in range(left, n):
            if s[left:i+1] in currArr:
                continue
            
            newArr = currArr.copy()
            newArr.append(s[left:i+1])
            
            self.backtrack(s, i+1, n, newArr)

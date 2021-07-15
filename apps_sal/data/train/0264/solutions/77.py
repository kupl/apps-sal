class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0
        
        max_length = 0
        
        duplicates = set([])
        from collections import deque
        queue = deque([])
        
        for idx, val in enumerate(arr):
            if val in duplicates or self.doesDuplicateExist(val):
                continue
            queue.appendleft((idx, val, len(val)))
            duplicates.add(val)
            
        n = len(arr) 
        
        while len(queue) != 0:
            idx, curr, curr_len = queue.pop()
            
            max_length = max(max_length, curr_len)
                
            for i in range(idx+1, n):
                newWord = curr + arr[i]
                if newWord in duplicates or self.doesDuplicateExist(newWord):
                    continue
                    
                queue.appendleft((i, newWord, len(newWord)))
                duplicates.add(newWord)
            
            
        return max_length
    
    def doesDuplicateExist(self, val):
        dup = set()
        
        for char in val:
            if char in dup:
                return True
            dup.add(char)
            
        return False
        


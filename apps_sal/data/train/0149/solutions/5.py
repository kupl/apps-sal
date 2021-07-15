class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        lengths = [[None, 0]]
        idx = 0
        
        while idx < len(s):
            current = lengths[-1][0]
            
            if current == s[idx]:
                lengths[-1][1] += 1
            else:
                lengths.append([s[idx], 1])
                current = s[idx]
                
            if lengths[-1][1] == k:
                lengths.pop()
                s = s[:idx - k + 1] + s[idx + 1:]
                idx -= k
                
            idx += 1
                    
        return s

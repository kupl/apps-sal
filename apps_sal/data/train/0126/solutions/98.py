class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        maxOccurrences = 0
        substrings = dict()
        
        for i in range(minSize, maxSize + 1):
            
            for j in range(len(s)):
                
                if i + j <= len(s):
                    
                    current = s[j:j+i]
                    
                    if len(set(current)) <= maxLetters:
                        
                        if current in substrings:
                            
                            substrings[current] += 1
                        
                        else:
                            
                            substrings[current] = 1
                    
                        if substrings[current] > maxOccurrences:
                            
                            maxOccurrences = substrings[current]
                            
                            
        
        return maxOccurrences

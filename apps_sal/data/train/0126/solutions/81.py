class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        SUB_LEN = len(s)
        cache = defaultdict(int)
        for start in range(SUB_LEN):
            
            for end in range(start + minSize-1, min(start + maxSize, SUB_LEN)):
                
                substring = s[start:end+1]
                
               
                if len(set(substring)) <= maxLetters:
                    
                    cache[substring] += 1 
        #print(cache.values())
        return max(cache.values()) if cache else 0
                    


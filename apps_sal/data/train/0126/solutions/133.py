class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        lookup = {}
        
        for size in range(minSize, maxSize + 1):
            for i in range(0, len(s) - size + 1):
                sub_s = s[i:i+size]
                if len(set(sub_s)) <= maxLetters:
                    if sub_s not in lookup:
                        lookup[sub_s] = 0
                    lookup[sub_s] += 1
                
        if not lookup:
            return 0

        return max(lookup.values()) 

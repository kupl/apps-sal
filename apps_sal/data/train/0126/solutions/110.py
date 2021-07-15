class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = 0
        ht = collections.Counter()
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                length = len(substring)
                if length >= minSize and length <= maxSize and len(set(substring)) <= maxLetters:
                    ht[substring]+=1
                elif length > maxSize:
                    break
                    
        return max(v for k,v in ht.items()) if ht else 0

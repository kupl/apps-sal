class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter=defaultdict(int)
        
        for i in range(len(s)):
            string=s[i:i+minSize]
            if len(Counter(string))<=maxLetters and len(string)>=minSize:
                counter[string]+=1
        return max(counter.values()) if counter else 0

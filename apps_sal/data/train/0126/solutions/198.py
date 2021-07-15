class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        mymap = {}
        
        for i in range(len(s)-minSize+1):
            if len(set(list(s[i:i+minSize]))) <= maxLetters:
                print(s[i:i+minSize])
                if s[i:i+minSize] in mymap:
                    mymap[s[i:i+minSize]] += 1
                else:
                    mymap[s[i:i+minSize]] = 1
        
        if not mymap:
            return 0
        
        return max(mymap.values())

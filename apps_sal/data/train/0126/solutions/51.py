class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = {}
        for outer in range(0,len(s)):
            if minSize + outer > len(s): break
            substring = s[outer:minSize+outer]
            while len(substring) <= maxSize and len(set(substring))<=maxLetters:
                if dic.get(substring): 
                    dic[substring] += 1
                else: dic[substring] = 1
                newIndex = outer + len(substring) + 1
                if not newIndex > len(s):
                    substring = s[outer:newIndex]
                else: break
        if dic:
            maxKey = max(dic,key=lambda key: dic[key])
            return dic[maxKey]
        else: return 0


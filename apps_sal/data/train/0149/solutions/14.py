class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s)<k:
            return s
        found = self.findStr(s, k)
        if not found:
            return s
        else:
            return self.removeDuplicates(s.replace(found, ''), k)
        
    def findStr(self, s:str, k:int):
        for i in range(len(s)):
            if (s[i]*k) in s:
                return s[i]*k
        return None

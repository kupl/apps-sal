class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        sliced = True
        while sliced == True:
            s, sliced = self.getSlices(s, k)
        return s
    
    def getSlices(self, s, k):
        sliced = False
        idx = set()
        i = 0
        while i < len(s):
            if s[i]*k == s[i:i+k]:
                idx.update(range(i, i+k))
                sliced = True
                i += k
            i += 1
        if sliced:
            new_str = ''.join([char for i, char in enumerate(s) if i not in idx])
            return new_str, sliced
        return s, sliced

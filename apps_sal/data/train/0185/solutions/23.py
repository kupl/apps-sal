class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set1 = set()
        for i in range(0, len(s) - k+1):
            set1.add(s[i:i+k])
        if(len(set1) >= 2**k):
            return True
        else:
            return False

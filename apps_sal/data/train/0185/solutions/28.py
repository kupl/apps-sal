class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hs = set()
        for i in range(len(s)-k+1):
            hs.add(s[i:i+k])
            if len(hs) == 2**k:
                return True
        print(hs)
        return False

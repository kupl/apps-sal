class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = 2**k
        k_string = set()
        for i in range(len(s)-k+1):
            if s[i:i+k] not in k_string:
                k_string.add(s[i:i+k])
                if len(k_string) == a:
                    return True
        return False

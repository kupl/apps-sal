class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i,j,k = 0,1,0
        while j + k < n:
            if s[i:i+k+1] == s[j:j+k+1]:
                k += 1
            elif s[i:i+k+1] < s[j:j+k+1]:
                i = j
                k = 0
                j = j + 1
            else:
                j += k + 1
                k = 0
        return s[i:j+k]

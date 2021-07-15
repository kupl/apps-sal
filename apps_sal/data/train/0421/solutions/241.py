# test case - \"acting\" for explanation
class Solution: 
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = 1
        k = 0
        n = len(s)
        while j+k < n:
            if s[i+k] == s[j+k]:
                k+=1
                continue
            elif s[i+k] > s[j+k]:
                j = j + k + 1
            else:
                i = max(i+k+1, j)
                j = i + 1
            k = 0
        return s[i:]


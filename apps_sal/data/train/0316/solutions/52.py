class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if(n < 2):
            return ''

        i = 1; j = 0
        f = [0 for _ in range(n)]
        
        while(i < n):
            if(s[i] == s[j]):
                j += 1
                f[i] = j
                i += 1

            elif(j > 0):
                j = f[j - 1]
            
            else:
                i += 1
        return s[:f[-1]]

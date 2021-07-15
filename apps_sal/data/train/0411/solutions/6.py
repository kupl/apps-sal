class Solution:
     def wordBreak(self, s, wordDict):
         f = [False for _ in range(len(s))]
         for i in range(len(s)):
             if(s[:i+1] in wordDict):
                 f[i] = True
                 continue
             for j in range(i):
                 if(f[j] and s[j+1:i+1] in wordDict):
                     f[i] = True
                     break
         return f[len(s)-1]


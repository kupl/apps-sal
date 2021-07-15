class Solution:
     def wordBreak(self, s, wordDict):
         """
         :type s: str
         :type wordDict: List[str]
         :rtype: bool
         """
         w = [0 for _ in range(len(s)+1)]
         
         for i in range(1,len(s)+1):
             if w[i] == 0 and s[:i] in wordDict:
                 w[i] = 1
             if w[i]:
                 if i == len(s):
                     return True
                 for j in range(i+1,len(s)+1):
                     if w[j] == 0 and s[i:j] in wordDict:
                         w[j] = 1
                     if j == len(s) and w[j] == 1:
                         return True
         
         return False

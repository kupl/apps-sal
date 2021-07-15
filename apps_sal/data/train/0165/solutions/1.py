class Solution:
     def findLongestWord(self, s, d):
         """
         :type s: str
         :type d: List[str]
         :rtype: str
         """
         def find(a,b):
             p = 0
             for c in b:
                 p = a.find(c,p) + 1
                 if p == 0:
                     return False
             return True
         
         ans = ''
         for word in d:
             if find(s,word):
                 if len(word) > len(ans):
                     ans = word
                 elif len(word) == len(ans) and word < ans:
                     ans = word
         return ans


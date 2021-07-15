class Solution:
     def findSubstring(self, s, words):
         """
         :type s: str
         :type words: List[str]
         :rtype: List[int]
         """
         lword = len(words[0])
         n = len(words)
         lwords = n * lword
         if not s or not lwords:
             return
         
         res = []
         dic = {} 
         for key in words:
             dic[key] = [0, 0]
         for key in words:
             dic[key][1] += 1
         for k in range(lword):
             i = k
             while i <= len(s)-lwords:
                 if not s[i:i+lword] in list(dic.keys()):
                     i += lword
                     continue
                 j = 0
                 start = i
                 while s[i:i+lword] in list(dic.keys()) and i<len(s):
                     key = s[i:i+lword]
                     dic[key][0] += 1
                     while dic[key][0] > dic[key][1]:
                         dic[s[start:start+lword]][0] -= 1
                         j -= 1
                         start += lword
                     j += 1
                     i += lword
                     if j==n:
                         res.append(start)
                         dic[s[start:start+lword]][0] -= 1
                         j -= 1
                         start += lword
                 for key in list(dic.keys()):
                     dic[key][0] = 0
         return res


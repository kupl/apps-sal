class Solution:
     def findSubstring(self, s, words):
         """
         :type s: str
         :type words: List[str]
         :rtype: List[int]
         """
         result = []
         lenWord = len(words[0])
         numOfWords = len(words)
         lenSubstring = lenWord * numOfWords
         dic = {}
         
         for word in words:
             if word in dic:
                 dic[word] += 1
             else:
                 dic[word] = 1
         
         for i in range(min(lenWord, len(s) - lenSubstring + 1)):
             curr = {}
             strStart = i
             wordStart = strStart
             while strStart + lenSubstring <= len(s):
                 word = s[wordStart: wordStart + lenWord]
                 wordStart += lenWord
                 if word not in dic:
                     strStart = wordStart
                     curr.clear()
                 else:
                     if word in curr:
                         curr[word] += 1
                     else:
                         curr[word] = 1
                     while curr[word] > dic[word]:
                         curr[s[strStart: strStart + lenWord]] -= 1
                         strStart += lenWord
                     if wordStart - strStart == lenSubstring:
                         result.append(strStart)
         return result


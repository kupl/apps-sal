class Solution:
     def findSubstring(self, s, words):
         if not s or not words: return []
         lens, lenw, numw = len(s), len(words[0]), len(words)
         res = []
         end = lens // lenw * lenw
         
         for i in range(lenw):
             start = sidx = i
             record = words[:]
             while sidx < end:              
                 tmp_sidx = sidx + lenw
                 tmp_word = s[sidx: tmp_sidx]
                 
                 if tmp_word in words:
                     if tmp_word in record:
                         record.remove(tmp_word)
                     elif s[start: start + lenw] != tmp_word:
                         sidx = start = start + lenw
                         record = words[:]
                         continue
                     else:
                         start = start + lenw
                 elif lens - tmp_sidx < lenw * numw:
                     break
                 else:
                     record = words[:]
                     start = tmp_sidx
                     
                 if not record: res.append(start)
                 sidx = tmp_sidx  
                 
         return res


class Solution:
     def frequencySort(self, s):
         """
         :type s: str
         :rtype: str
         """
         charToFreq = {}
         freqToChar = {}
         for c in s:
             if c not in charToFreq:
                 charToFreq[c] = 0
             charToFreq[c] += 1
         print(charToFreq)
         for key, value in list(charToFreq.items()):
             if value not in freqToChar:
                 freqToChar[value] = []
             freqToChar[value].append(key)
         print(freqToChar)
         result = []
         for key in sorted(freqToChar, reverse = True):
             for char in freqToChar[key]:
                 result += [char] * key
         return "".join(result)


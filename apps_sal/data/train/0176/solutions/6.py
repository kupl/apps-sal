class Solution:
     def isScramble(self, s1, s2):
         """
         :type s1: str
         :type s2: str
         :rtype: bool
         """
         
         """
         CHECKING TWO STRINGS ARE ANAGRAMS IS FASTER BY SORTING THAN BY COUNTE (AT WHAT LEN DOES THIS FLIP)
         RETURNING WHEN SORTED(S1) != SORTED(S2[LEFT:RIGHT+1]) GOT MY CODE FROM 1800 MS TO 150MS.
         """
         
         def getfromdictt(strr, left, right):
             args = (strr, s2[left:right+1])
             if args in dictt:
                 return dictt[args]
             res = scramble(strr, left, right)
             dictt[args] = res
             return res
         
         def putindictt(strr, left, right, val):
             dictt[(strr, s2[left:right+1])] = val
             return val
         
         def scramble(s1, left, right):
             
             if sorted(s1) != sorted(s2[left:right+1]):
                 return putindictt(s1, left, right, False)
             # if collections.Counter(s1) != collections.Counter(s2[left:right+1]): return False
             
             
             if s2[left:right+1] == s1:
                 return putindictt(s1, left, right, True)
             
             for i in range(len(s1)-1):
                 leftstr, rightstr = s1[:i+1], s1[i+1:]
                 leftmatch = getfromdictt(leftstr, left, left+i)
                 rightmatch = getfromdictt(rightstr, left+i+1,right)
                 
                 if leftmatch and rightmatch:
                     return putindictt(s1, left, right, True)
                 
                 flipleftmatch = getfromdictt(rightstr, left, left + len(rightstr)-1)
                 fliprightmatch = getfromdictt(leftstr, left + len(rightstr), right)
 
                 if flipleftmatch and fliprightmatch:
                     return putindictt(s1, left, right, True)
             
             return putindictt(s1, left, right, False)
         
         dictt = {}
         return scramble(s1, 0, len(s1)-1)


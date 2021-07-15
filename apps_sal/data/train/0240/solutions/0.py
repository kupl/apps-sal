class Solution:
     def frequencySort(self, s):
         """
         :type s: str
         :rtype: str
         """
         counter = collections.Counter(s)
         colls = sorted(counter.items(), key=lambda k: k[1], reverse=True)
         res = ''
         for k, v in colls:
             res += k * v
         return res

class Solution:
     def frequencySort(self, s):
         """
         :type s: str
         :rtype: str
         """
         '''
         cnt = collections.Counter(s)
         tmp = list(k*v for k, v in cnt.items())
         res = sorted(tmp, key=len, reverse=True)
         return ''.join(res)
         '''
         res = ''
         cnt = collections.Counter(s)
         tmps = cnt.most_common()
         for tmp in tmps:
             res += tmp[0]*tmp[1]
         return res


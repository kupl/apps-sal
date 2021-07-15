class Solution:
     def countSubstrings(self, s):
         """
         :type s: str
         :rtype: int
         """
         ss = "$#"
         for i in s:
             ss += i + '#'
         ss += '@'
         r = [0] * (len(ss) + 1) 
         pos = 0
         ma = 0
         for i in range(1, len(ss) - 1):
             if ma > i:
                 r[i] = min(r[pos - (i - pos)], ma - i)
             else:
                 r[i] = 1
             while ss[i + r[i]] == ss[i - r[i]]:
                 r[i] += 1
             # print(i, r[i])
             if r[i] + i > ma:
                 pos, ma = i, r[i] + i
         ans = sum(int(l/2) for l in r)
         return ans

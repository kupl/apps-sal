class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 1
        for i in range(2 ** (n - 1)):
            b = '1' + bin(i)[2:].zfill(n - 1) + '1'
            pr = 0
            w = set()
            flag = True
            for k in range(1, n + 1):
                if k == n or b[k] == '1':
                    chrs = s[pr: k]
                    if chrs in w:
                        flag = False
                        break
                    w.add(chrs)
                    pr = k
            if flag:
                ans = max(ans, len(w))
        return ans


#         @lru_cache(None)
#         def dp(s):
#             if s == '':
#                 return set()
#             if len(s) == 1:
#                 return set([s[0]])
#             ans = 0
#             com = set()
#             for i in range(1,len(s)+1):
#                 l = set([s[:i]])
#                 r = dp(s[i:])
#                 if i != len(s) and len(r) == 0: # unvalid right
#                     continue

#                 if len(l.intersection(r)) == 0:
#                     if len(l) + len(r) > ans:
#                         ans = len(l) + len(r)
#                         com = l.union(r)
#             return com

#         print(dp(s))
#         return len(dp(s))

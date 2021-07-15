from functools import reduce
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            # print(26, L, mod)
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
        
#         s = [ord(num) - ord(\"a\") for num in S]
        
#         mod = 10 ** 9 + 7
#         def check(l):
#             cur = 0
#             seen = set()
#             maxBASE = pow(26, l-1, mod)
#             for i in range(len(s)):
#                 if i < l:
#                     cur = (cur * 26 + s[i]) % mod
#                 else:
#                     cur -= maxBASE * s[i-l]
#                     cur = (cur * 26 + s[i]) % mod
#                 if i == l-1:
#                     seen.add(cur)
#                 elif i >= l:
#                     if cur in seen:
#                         return i-l+1
#                     else:
#                         seen.add(cur)
#             return 0
                
                
                
        
#         l = 1
#         r = len(S) - 1
#         res = -1
#         while l < r:
#             m = (l+r) // 2
#             pos = check(m)
#             if pos:
#                 l = m 
#                 res = pos
#             else:
#                 r = m - 1
#         return S[res:res + l]
            
        
            


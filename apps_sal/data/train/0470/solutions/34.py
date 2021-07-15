class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        m = collections.Counter(A)
        res = 0
        for n0, n1 in itertools.combinations_with_replacement(m, 2):
            n2 = target - n0 - n1
            if n0 == n1 == n2:
                res += m[n0] * (m[n0] - 1) * (m[n0] - 2) // 6
            elif n0 == n1 != n2:
                res += (m[n0] * (m[n0] - 1) // 2) * m[n2]
            elif max(n0, n1) < n2:
                res += m[n0] * m[n1] * m[n2]
            # print((n0, n1, n2), 'res', res)
            
        return res % (10**9 + 7)
                
        
        
        
        
        
        
#         m = collections.Counter(A)
#         keys = sorted(m.keys())
#         def twoSums(left, target):
#             res = 0
#             for i in range(left, len(keys)):
#                 n = keys[i]
#                 if n * 2 > target:
#                     break
#                 if n * 2 == target:
#                     res += m[n] * (m[n] - 1) // 2
#                     break
#                 res += m[n] * m[target - n]
#             return res
        
#         res = 0
#         for i, n in enumerate(keys):
#             if n * 3 > target:
#                 break
#             if n * 3 == target:
#                 res += m[n] * (m[n] - 1) * (m[n] - 2) // 6
#                 break
            
#             res += (m[n] * (m[n] - 1) // 2) * m[target - n * 2]
#             count, m[n] = m[n], 0
#             res += count * twoSums(i + 1, target - n)
#         return res % (10**9 + 7)
        
        


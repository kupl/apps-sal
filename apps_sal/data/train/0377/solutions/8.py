class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        
#         # O(N) solution -- TLE
#         i = 1 # multiplier of A
#         j = 1 # multiplier of B
        
#         res = 0
        
#         while N>0:
#             if A*i < B*j:
#                 res = A*i
#                 i += 1
#             elif A*i > B*j:
#                 res = B*j
#                 j += 1
#             else:
#                 res = A*i
#                 i += 1
#                 j += 1
#             N-=1
        
#         return res%(10**9+7)
    
        # O(logN) solution -- binary search
        def min_common_divisor(a, b):
            less = min(a, b)
            more = max(a, b)
            for i in range(1, less+1):
                if more*i % less == 0:
                    return more*i
            return a*b
        
        _cd = min_common_divisor(A, B)

        min_ = min(A, B)
        l, r = min_, min_*N+1
        while l<r:
            m = (l+r)>>1

            if m//A+m//B-m//_cd < N:
                l = m + 1
            elif m//A+m//B-m//_cd > N:
                r = m
            else:
                if m%A==0 and m%B==0:
                    return m % (10**9+7)
                else:
                    r = m

        return l % (10**9+7)

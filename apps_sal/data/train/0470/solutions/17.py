from collections import Counter
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        mp = Counter(A)
        total = 0
        mpow = 10**9 + 7
        for i in range(101):
            for j in range(i, 101):
                calc = target-(i+j)
                if calc > 100 or calc < 0:
                    continue
                if i == j == calc:
                    x = mp[i]
                    top_row = x*(x-1)*(x-2)
                    top_row /=6
                    total += top_row#nC3
                elif i == j != calc:
                    x = mp[i]
                    total += ((x*(x-1))/2) * mp[calc]
                elif i < j < calc:
                    total += mp[i]*mp[j]*mp[calc]
        return int(total % mpow)
        

#     def threeSumMulti(self, A: List[int], target: int) -> int:
#         total = 0
#         A.sort()
#         mod_pow = 10**9 + 7
#         for i in range(len(A)):
#             l = i+1
#             r = len(A)-1
#             while l < r:
#                 calc = A[i] + A[l] + A[r]
#                 if calc > target:
#                     r -= 1
#                 elif calc < target:
#                     l += 1
#                 elif A[l] == A[r]:
#                     x = r-l+1
#                     comb = (x*(x-1)) / 2
#                     total += comb
#                     break
#                 else:
#                     lcount = 1
#                     rcount = 1
#                     while l+1 < r and A[l] == A[l+1]:
#                         lcount += 1
#                         l += 1
#                     while r-1 > l and A[r] == A[r-1]:
#                         rcount += 1
#                         r -= 1
#                     total += (lcount*rcount)
#                     l += 1
#                     r -= 1                    
                
#         return int(total%mod_pow)


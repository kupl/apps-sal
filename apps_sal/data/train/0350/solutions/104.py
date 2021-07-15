from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.helper(A, K) - self.helper(A, K-1)
    def helper(self, A, K):
        currSum = 0 
        d = Counter() 
        i = 0 
        for j in range(len(A)): 
            d[A[j]] += 1
            while(len(d) > K): 
                d[A[i]] -= 1
                if not d[A[i]]: del d[A[i]]
                i+= 1
            currSum += ((j-i)+1)
        return currSum
#         mapp={}
#         n=len(A)
#         j=0
#         ans=0
        
#         for i,c in enumerate(A):
#             mapp[c]=i # last position of c
#             while (len(mapp)>K):
#                 if j==mapp[A[j]]:
#                     del mapp[A[j]]
#                 j+=1
#             ans+=i-j+1
#         return ans


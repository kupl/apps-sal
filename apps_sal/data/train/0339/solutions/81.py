from collections import Counter
class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        def getTriplets(A, B):
            m, n = len(A), len(B)
            ans = 0
            counter = Counter()
            for j in range(n):
                for k in range(j+1,n):
                    prod = B[j]*B[k]
                    counter[prod] += 1
            for i in range(m):
                prod = A[i]**2
                ans += counter[prod]
            return ans 
        return getTriplets(A,B) + getTriplets(B,A)

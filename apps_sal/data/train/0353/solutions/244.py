from itertools import combinations

class Solution:
    def numSubseq(self, A, target) -> int:
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        
        ans = 0
        j = N - 1
        for i in range(N):
            while i < j and A[i] + A[j] > target:
                j -= 1
                
            if A[i] + A[j] <= target:
                ans += pow(2, j - i, MOD)
                ans %= MOD
                
        return ans


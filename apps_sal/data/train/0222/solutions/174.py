class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        fibHash = {} 
        ans = 0
        
        n = len(A)
        for i in range(1, n):
            for j in reversed(range(i)):
                f1 = A[i] - A[j]
                size = fibHash[(A[j], A[i])] = fibHash.get((f1, A[j]), 1) + 1                
                ans = max(ans, size)
                
        return ans if ans > 2 else 0

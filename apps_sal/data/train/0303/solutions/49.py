class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        def maxSum(i, mem):
            if i in mem: return mem[i]
            
            if len(A) - i <= K:
                mem[i] = max(A[i:]) * (len(A) - i)
                return mem[i]
            
            ans = -float('inf')
            for j in range(i+1, i+1+K):
                if j > len(A): break
                ans = max(ans, max(A[i:j]) * (j-i) + maxSum(j, mem))
            mem[i] = ans
            return mem[i]
        
        mem = {}
        return maxSum(0, mem)

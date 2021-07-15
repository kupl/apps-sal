class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        def DPHelper(index):
            if(index >= len(A)):
                return 0
            
            if(memo.get(index) is not None):
                return memo[index]
            
            res = 0
            curr_max = 0
            
            for i in range(index, min(index + K, len(A))):
                curr_max = max(curr_max, A[i])
                res = max(res, (curr_max * (i - index + 1)) + DPHelper(i + 1))
            
            memo[index] = res
            
            return res
        
        memo = {}
        
        return DPHelper(0)

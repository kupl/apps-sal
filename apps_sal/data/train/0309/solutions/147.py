class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        
        dp = [{0: 1}]
        
        max_val = 1
        
        for i in range(1, len(A)):
            dp.append({0: 1})
                        
            for j in range(i):
                diff = A[i] - A[j]
                diff_val = 2
                
                if diff in dp[j]:
                    diff_val = dp[j][diff] + 1
                
                dp[-1][diff] = diff_val

                max_val = max(max_val, diff_val)
                    
        return max_val

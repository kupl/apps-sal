class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr))
        dp[0] = arr[0]
        for i, val in enumerate(arr):
            if i == 0:
                continue
            cur_max = val + dp[i - 1]
            cur_k = 1
            m = val
            while(i - cur_k >= 0 and cur_k < k):
                m = max(m, arr[i - cur_k])
                if i - cur_k == 0:
                    cur_max = max(cur_max, m * (cur_k + 1))
                else:
                    cur_max = max(cur_max, (m * (cur_k + 1)) + dp[i - cur_k - 1])
                cur_k += 1
            dp[i] = cur_max
        return dp[-1]

        '''    
        
        
        
        
        
        
        '''

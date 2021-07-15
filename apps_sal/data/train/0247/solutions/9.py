class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        record = collections.defaultdict()
        record[0] = 0
        l1 = l2 = float('Inf')
        tmp_sum = 0
        res = float('Inf')
        dp = [float('Inf') for _ in range(len(arr) + 1)]
        
        for i in range(len(arr)):
            tmp_sum += arr[i]
            if tmp_sum - target in record:
                dp[i+1] = i - record[tmp_sum - target] + 1
                res = min(res, dp[i+1] + dp[record[tmp_sum - target]])
            
            record[tmp_sum] = i + 1
            
            dp[i+1] = min(dp[i+1], dp[i])
        
            
        return res if res<float('Inf') else -1
        


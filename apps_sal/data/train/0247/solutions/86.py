class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        sums, res = 0, float('inf')
        
        sum_record = {0: -1}
        
        for i, num in enumerate(arr):
            sums += num
            dp[i] = dp[i - 1]
            if sums - target in sum_record:
                cur_len = i - sum_record[sums - target]
                if i - cur_len >= 0:
                    res = min(res, cur_len + dp[i - cur_len])
                dp[i] = min(dp[i - 1], cur_len)
            sum_record[sums] = i
        return res if res != float('inf') else -1


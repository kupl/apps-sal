class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [10000000] * n
        
        presum = {}
        presum[0] = -1
        s = 0
        bestsofar = 10000000
        ans = 10000000
        for i in range(n):
            s += arr[i]
            if s - target in presum:
                j = presum[s - target]
                bestsofar = min(bestsofar, i - j)
                
                if j >= 0:
                    ans = min(ans, dp[j] + i - j)
            
            presum[s] = i
            dp[i] = bestsofar

        return ans if ans < 10000000 else -1


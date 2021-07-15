class Solution:
  def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sums = {0:-1}
        prefix = 0
        dp = [math.inf for _ in range(len(arr)+1)]
        ans = math.inf
        for idx, num in enumerate(arr):
            prefix += num
            dp[idx+1] = min(dp[idx+1], dp[idx])
            if prefix-target in sums:
                ans = min(ans, idx-sums[prefix-target] + dp[sums[prefix-target]+1])
                dp[idx+1] = min(dp[idx+1], idx-sums[prefix-target])
            sums[prefix] = idx
        
        return ans if ans != math.inf else -1

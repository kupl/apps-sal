class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # Make a dp[n][2], where dp[i][0] is the largest sum of subarry ending at i without removing any element and dp[i][1] represents largest sum of subarray ending at i after removal of one element.
        
        n = len(arr)
        dp = [ [0 for _ in range(2)] for _ in range(n) ]
        dp[0] = [arr[0]] * 2
        for i in range(1, n):
            dp[i][0] = max(arr[i], dp[i-1][0] + arr[i])
            dp[i][1] = max(dp[i][0], dp[i-1][1] + arr[i])
            if i >= 2:
                dp[i][1] = max(dp[i][1], dp[i-2][0] + arr[i])     
        return max(map(lambda l: max(l), dp))

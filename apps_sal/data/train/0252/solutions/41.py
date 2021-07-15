class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 傻瓜一点想法  DP 
        # 每个点 左边loop 当前最小值和左边最小值+1
        # 有点每个点  同理
       
        dp = [0] + [n + 2] * n
        for i , cur in enumerate(ranges):
            for j in range(max(0,i-cur+1),min(n,i+cur)+1):
                dp[j] = min(dp[j], dp[max(0,i-cur)] + 1)
        return dp[n] if dp[n] < n + 2 else -1       # 0-5 最多有6个 n+1

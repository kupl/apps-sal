class Solution:
    def maximumSum(self, a: List[int]) -> int:
        max_so_far = -sys.maxsize
        max_ending_here = 0
        size=len(a)
        dp=[-sys.maxsize]*size
        dp[0]=a[0]
        dp1=[-sys.maxsize]*size
        dp1[0]=a[0]
        for i in range(1, size): 
            dp[i]=max(a[i],dp[i-1]+a[i])
            dp1[i]=max(a[i],dp1[i-1]+a[i])
            if i>=2:
                dp1[i]=max(dp1[i],dp[i-2]+a[i])
        return max(dp1)
        


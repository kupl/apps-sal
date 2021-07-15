class Solution:
    def maxSum(self, x: List[int], y: List[int]) -> int:
        def f(i,p):
            if (p==0 and i>=len(x)) or (p==1 and i>=len(y)):return 0
            if (i,p) in dp:return dp[i,p]
            ans=f(i+1,p)
            if p==0:
                if x[i] in b :ans=max(f(b[x[i]]+1,1-p),ans)
            else:
                if y[i] in a:ans=max(f(a[y[i]]+1,1-p),ans)
            dp[i,p]=ans+(x[i] if p==0 else y[i])
            return dp[i,p]
        a,b,dp={},{},{}
        for j,i in enumerate(x):a[i]=j
        for j,i in enumerate(y):b[i]=j
        return max(f(0,0),f(0,1))%(10**9+7)

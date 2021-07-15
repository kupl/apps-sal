class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        st,n = 0,len(s)
        seg = []
        for i in range(1,n):
            if s[i]!=s[i-1]:
                seg.append((s[i-1],i-st))
                st=i
        seg.append((s[n-1],n-st))
        n=len(seg)
        dp = [[None]*(k+1) for _ in range(n)]
        def solve(i,ki):
            if i==n:
                return 0
            if dp[i][ki] is not None:
                return dp[i][ki]
            dp[i][ki]=float('inf')
            for j in range(min(ki+1,seg[i][1]+1)):
                if seg[i][1]!=j:
                    dp[i][ki]=min(dp[i][ki],1+(len(str(seg[i][1]-j)) if seg[i][1]-j!=1 else 0)+solve(i+1,ki-j))
                else:
                    dp[i][ki]=min(dp[i][ki],solve(i+1,ki-j))
            ps = 0
            curr=0
            for j in range(i+1,n):
                if ki>=ps and seg[j][0]==seg[i][0]:
                    for kj in range(ki-ps+1):
                        if kj<seg[i][1]+seg[j][1]+curr:
                            dp[i][ki]=min(dp[i][ki],1+(len(str(seg[i][1]+curr+seg[j][1]-kj)) if seg[i][1]+curr+seg[j][1]-kj!=1 else 0)+solve(j+1,ki-ps-kj))
                        elif kj==seg[i][1]+seg[j][1]+curr:
                            dp[i][ki]=min(dp[i][ki],solve(j+1,ki-ps-kj))
                        else:
                            break
                ps+=(seg[j][1] if seg[j][0]!=seg[i][0] else 0)
                curr+=(seg[j][1] if seg[j][0]==seg[i][0] else 0)
            return dp[i][ki]
        return solve(0,k)

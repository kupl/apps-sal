from collections import defaultdict as dd
class Solution:
    def countTriplets(self,a):
        n=len(a)
        cnt=0
        dp=[[-float('inf')]*n for i in range(n)]
        for i in range(n):
            curr=a[i]
            dp[i][i]=curr
            for j in range(i+1,n):
                curr=curr^a[j]
                dp[i][j]=curr
        for i in range(1,n):
            map=dd(int)
            for j in range(i):
                map[dp[j][i-1]]+=1
            for j in range(i,n):
                cnt+=map[dp[i][j]]
                if(map[dp[i][j]]==0):del map[dp[i][j]]
        return cnt

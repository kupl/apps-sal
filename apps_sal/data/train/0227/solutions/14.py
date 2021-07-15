def solve(arr,n,k):
    prefix=[0]
    for i in range(0,n):
        if(arr[i]==0):
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])
    low=0
    high=n+1
    ans=0
    while(low<high):
        f=0
        mid=low+(high-low)//2
        for i in range(mid,n+1):
            if(prefix[i]-prefix[i-mid]<=k):
                ans=max(ans,mid)
                f=1
        if(f==1):
            low=mid+1
        else:
            high=mid
    return ans
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        return solve(A,len(A),K)


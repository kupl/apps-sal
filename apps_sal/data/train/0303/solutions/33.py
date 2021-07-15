class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        memo=[0]*n
        for i in range(n):
            if i<k:
                memo[i]=(i+1)*max(arr[:i+1])
            else:
                memo[i]=max(memo[i-j-1]+(j+1)*max(arr[i-j:i+1]) for j in range(k))
        return memo[-1]

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        s=sum(arr)
        def kadane(arr):
            
            cur=m=arr[0]
            for i in range(1,len(arr)):
                cur=max(arr[i],cur+arr[i])
                m=max(cur,m)
            return m
        if not arr:
            return 0
        if k==1:
            return max(0,kadane(arr)%(10**9+7))
        else:
            return max(0, (k - 2) * max(s, 0) + kadane(arr + arr)) % (10 ** 9 + 7)


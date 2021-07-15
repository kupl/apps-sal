class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cursum = 0
        ans = 0
        if(arr[0]%2):
            cursum =1
            ans = 1
        for i in range(1,len(arr)):
            if(arr[i]%2):
                cursum = i - cursum + 1
            ans = ans +cursum
        return(ans%(10**9+7))

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = len(arr)
        ans = 0
        x = 0
        running_sum = sum(arr[0:k])
        if running_sum/k >= threshold: ans+=1
        while k+x < l:            
            running_sum+=arr[k+x]-arr[x]
            if running_sum/k >= threshold: ans+=1
            x+=1
        return ans


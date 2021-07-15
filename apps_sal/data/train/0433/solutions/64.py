class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        running_sum = sum(arr[0:k])
        if running_sum/k >= threshold: ans+=1
        for x in range(len(arr)-k):
            running_sum+=arr[k+x]-arr[x]
            if running_sum/k >= threshold: ans+=1
        return ans


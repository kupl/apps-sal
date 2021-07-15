class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return self.dp(arr, 0, k, {})
    
    
    def dp(self, arr, i, k, hashmap):
        if i>=len(arr):
            return 0
        
        if i in hashmap:
            return hashmap[i]
        
        largest = 0
        ans = 0
        for idx in range(k):
            if idx + i >=len(arr):
                break
            largest = max(largest, arr[i+idx])
            ans = max(ans, largest*(idx+1) + self.dp(arr, i+idx+1, k, hashmap))
        
        hashmap[i] = ans
        return ans
            


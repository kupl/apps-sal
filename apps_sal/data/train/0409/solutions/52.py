class Solution:
    def kadanes(self,arr,n):
        max_so_far = 0
        max_here = 0
        
        for i in range(n):
            max_here += arr[i % len(arr)]
            if max_so_far < max_here:
                max_so_far = max_here
            if max_here < 0:
                max_here = 0
        return max_so_far
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        
        if k >= 2:
            return self.kadanes(arr,len(arr)*2) + (k-2) * max(sum(arr),0) % (10**9+7)
        else:
            return self.kadanes(arr,len(arr)) % (10**9+7)

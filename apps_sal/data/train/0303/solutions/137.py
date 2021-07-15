class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        res = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            for j in range(1, k + 1):
                if i - j > -1:
                    res[i] = max(res[i], res[i - j] + max(arr[i - j : i]) * j)
        
        return res[-1] 

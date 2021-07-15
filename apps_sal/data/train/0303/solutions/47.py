class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        rec = {}
        def helper(idx):
            if idx in rec:
                return rec[idx]            
            if len(arr)-idx <= k:
                temp = max(arr[idx:])*(len(arr)-idx)
                rec[idx] = temp
                return temp
            pre_max = float('-inf')
            temp = float('-inf')
            for j in range(idx, min(idx+k, len(arr))):
                pre_max = max(pre_max, arr[j])
                temp = max(temp, pre_max*(j-idx+1)+helper(j+1))
            rec[idx] = temp
            return temp
        
        return helper(0)

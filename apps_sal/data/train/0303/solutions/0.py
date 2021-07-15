class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        res = [0]
        
        for idx, val in enumerate(arr):
            max_val, cur_val = 0, 0
            
            for i in range(max(0, idx-k+1), idx+1)[::-1]:
                
                if arr[i] > max_val:
                    max_val = arr[i]
                    
                if res[i] + (idx-i+1)*max_val > cur_val:
                    cur_val = res[i] + (idx-i+1)*max_val
                    
            res.append(cur_val)
        return res[-1]

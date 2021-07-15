class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sum2_idx = defaultdict(int)
        prefix_sum2_idx[0] = -1
        prefix_sum = 0 
        n = len(arr)
        
        for i in range(n):
            prefix_sum += arr[i]
            prefix_sum2_idx[prefix_sum] = i
        
        prefix_sum = 0
        l_min_len = float('inf')
        min_len = float('inf')
        
        for i in range(n):
            prefix_sum += arr[i]
            # find min length whose right end point is i 
            if prefix_sum - target in prefix_sum2_idx:
                l_min_len = min(l_min_len, i - prefix_sum2_idx[prefix_sum - target])
            
            # find min length whose left start point is i + 1
            if prefix_sum + target in prefix_sum2_idx:
                min_len = min(min_len, prefix_sum2_idx[prefix_sum + target] - i + l_min_len)
            
        return -1 if min_len == float('inf') else min_len
        
        


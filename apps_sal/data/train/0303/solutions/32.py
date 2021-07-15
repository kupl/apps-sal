class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        if not arr:
            return 0
        
        
        local_max = {(idx, idx+1) :arr[idx] for idx in range(len(arr))}
        for l in range(2, k+1):
            for start in range(len(arr)-l+1):
                local_max[(start, start+l)] = max(local_max[(start, start+l-1)], local_max [(start+1, start+l)])
        
                
        f = [0]
        for end in range(1, len(arr)+1):
            _local = 0
            for start in range(max(0, end-k), end):
                _local = max(f[start]+local_max[(start, end)]*(end-start), _local)
            f.append(_local)
        return f[-1]
    
        


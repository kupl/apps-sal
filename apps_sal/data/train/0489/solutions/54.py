class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        #11M coding start
        
        min_map, max_map = {}, {}
        
        for i, v in enumerate(A):
            min_map[v] = min(i, min_map.get(v, i))
            max_map[v] = max(i, max_map.get(v, i))
        
        min_idx = None
        res = 0
        for i in range(0, 50001):
            if i not in min_map:
                continue
            
            if min_idx is None:
                min_idx = min_map[i]
            else:
                min_idx = min(min_idx, min_map[i])

            if max_map[i] > min_idx:
                res = max(res, max_map[i] - min_idx)
                
        return res


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        A_idx = []
        for idx, a in enumerate(A):
            A_idx.append((a, idx))
            
        A_idx_sorted = sorted(A_idx, key = lambda x: x[0])
        
        mn = float('inf')
        res = 0
        for a, idx in A_idx_sorted:
            res = max(res, idx - mn)
            mn = min(mn, idx)
        return res


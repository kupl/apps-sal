class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target: return max(arr)
        lo = 0
        hi = target
        
        best = float('inf')
        res = float('inf')
        
        while lo < hi:
            mid = (lo + hi) // 2
            s = sum(min(x, mid) for x in arr)
            diff = abs(s-target)
            if diff < best or (diff == best and mid < res):
                res = mid
                best = diff

            if s > target:
                hi = mid
            else:
                lo = mid + 1
        
        return res


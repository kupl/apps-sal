class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calculate(value):
            s = 0
            for x in arr:
                s += min(x, value)
            
            return s
        
        l, r = 1, max(arr)
        while l <= r:
            mid = l + (r - l) // 2
            if calculate(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if abs(calculate(l - 1) - target) <= abs(calculate(l) - target):
            return l - 1
        
        return l
        


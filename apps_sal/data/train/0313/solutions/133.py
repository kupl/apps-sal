class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        l, r = 1, max(bloom) + 1
        
        def do(t):
            j = 0
            ct = 0
            while j < len(bloom):
                i = j
                a = 0
                while i < len(bloom) and bloom[i] <= t:
                    a += 1
                    if a == k:
                        ct += 1
                        break
                    i += 1

                if ct == m:
                    return True
                
                j = i + 1
            return False
        
        while l < r:
            mid = (l + r) // 2
            
            if not do(mid):
                l = mid + 1
            else:
                r = mid
        
        return l if l <= max(bloom) else -1

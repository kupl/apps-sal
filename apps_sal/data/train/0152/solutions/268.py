class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        @lru_cache(None)
        def helper(gap):
            prev = 0
            cnt = 1
            while cnt < m:
                idx = prev + 1
                while idx < len(position) and position[idx] - position[prev] < gap:
                    idx += 1
                if idx >= len(position): break    
                prev = idx
                cnt += 1
            return cnt == m
        
        lb, ub = 1, position[-1] - position[0] + 1
        while lb < ub:
            mid = lb + (ub - lb)//2
            if helper(mid):
                if not helper(mid + 1): return mid
                else: lb = mid + 1
            else: ub = mid
                
        return lb

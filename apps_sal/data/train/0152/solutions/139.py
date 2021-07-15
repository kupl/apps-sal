class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def check(force):
            k = m - 1
            pre = 0
            i = 1
            while i < n:
                while i < n and position[i] - position[pre] < force:
                    i += 1
                if i < n:
                    k -= 1
                if k == 0:
                    return True
                pre = i
                i += 1
            return False
        lo, hi = 1, position[-1]
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1

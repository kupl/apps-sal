class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canCarry(cap):
            cur,d = 0, 1
            for w in weights:
                if w > cap: return False
                cur += w
                if cur > cap:
                    cur = w
                    d += 1
                if d > D: return False
            return cur <= cap
        
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if canCarry(m): r = m
            else: l = m + 1
        return l

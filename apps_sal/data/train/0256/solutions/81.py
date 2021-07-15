class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def condition(arr, k, h):
            res = 0
            for i in arr:
                res += math.ceil(i/k)
            if res <= h:
                return True
            return False
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            if condition(piles, m, H):
                r = m
            else:
                l = m + 1
        
        return l

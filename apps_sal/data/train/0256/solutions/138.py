class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        
        while lo<hi:
            mid=(lo+hi)//2
            
            cur_cap, num_hrs = 0, 0
            for p in piles:
                cur_cap = p
                if cur_cap<=mid:
                    num_hrs+=1
                else:
                    num_hrs+=(cur_cap//mid)+1

            if num_hrs>H:
                lo=mid+1
            else:
                hi=mid
        
        return lo


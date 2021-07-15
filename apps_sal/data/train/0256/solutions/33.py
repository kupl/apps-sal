class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        #piles.sort()
        
        lo, hi = 1, max(piles)
        ans = hi
        while lo <= hi:
            k = (lo + hi) // 2
            time = 0
            for i in piles:
                t = int(ceil(i / k))
                if not t:
                    t += 1
                time += t
                
                if time > H:
                    break
                
            #print(k, time)
            if time <= H:
                hi = k - 1
                ans = k
            else:
                lo = k + 1
        
        return ans

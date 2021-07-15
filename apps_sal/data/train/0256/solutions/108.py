class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == 1:
            return piles[0]//H if piles[0]%H == 0 else piles[0]//H + 1
        
        l = sum(piles)//H 
        h = max(piles)*len(piles)//H + 1
        
        # def feasible(c):
        #     t = 0
        #     s = 0
        #     for n in piles:
        #         if n <= c: #can finish this pile
        #             t += 1
        #         else: 
        #             t += n//c if n%c == 0 else n//c + 1
        #         #print(n, t)
        #     if t <= H:
        #         return True
        #     return False
        def feasible(k): #from solution, much shorter and cleaner
            return sum((p-1)//k + 1 for p in piles) <= H
        
        while l < h:
            mid = (l+h)//2
            #print(l, h, mid)
            if feasible(mid):
                h = mid #search if smaller capacity possible
            else:
                l = mid + 1
        return l

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        k = sum(piles)//H
        if k == 0: return 1 #if H is more than sum of all piles
        while True:
            h = 0
            prev = k
            #print(k)
            for p in piles:
                print(p,k)
                if p > 1:
                    h += (p-1)//k+1
                else:
                    h += 1
                if h > H:
                    #print(k,h)
                    break
            if h <= H:
                return k 
            k += 1

class Solution:
    def check(self, w, cap, D):
            c = 0
            d = 0
            i = 0
            while(i<len(w)):
                c+=w[i]
                if c>cap:
                    d += 1
                    c = w[i]
                i+=1
            return d
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l , h= max(weights), sum(weights)
        while(l<=h):
            m = (l+h)//2
            if self.check(weights, m, D)>=D:
                l = m + 1
            else:
                h = m - 1
        return l 


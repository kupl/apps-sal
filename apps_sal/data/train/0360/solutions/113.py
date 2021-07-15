class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(capacity, D):
            d = 0
            i = 0
            c = capacity
            while(d < D):
                if(i == len(weights)):
                    return True
                if(weights[i] <= c):
                    if(weights[i] > capacity):
                        return False
                    c -= weights[i]
                    i+=1
                else:
                    c = capacity
                    d += 1
            return False
        l=0; r=max(weights)*len(weights)
        while(l<r):
            mid = l + (r-l)//2
            if(check(mid, D)):
                r = mid
            else:
                l = mid+1
        return l

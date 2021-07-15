class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def count(k):
            
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] + k - 1) // k
            return hours
                
        l = 1
        r = 1000000000
        while l < r:
            m = l + (r - l) //2
            if count(m) > H:
                l = m + 1
            else:
                r = m
        return l
                


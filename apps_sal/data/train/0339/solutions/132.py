class Solution:
    def fact(self, n):   
        res = 1
        for i in range(2, n+1): 
            res = res * i 
        return res 

    def getCombo(self, n):
        return int(self.fact(n) / (self.fact(2)  
                * self.fact(n - 2))) 
    
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        #similar to the 2 sum problem- keep a dictionary for each list 
        d1 = {}
        for n in nums1:
            if n not in d1:
                d1[n] = 1
            else:
                d1[n]+=1
        d2 = {}
        for n in nums2:
            if n not in d2:
                d2[n] = 1
            else:
                d2[n]+=1
        tot = 0
        sq1 = 0
        
        for n in nums1:
            s = n*n
            for d in d2:
                if s%d == 0:
                    div = s//d
                    if div in d2:
                        if div == d:
                            sq1+=self.getCombo(d2[div])
                        else:
                            tot+=(d2[div]*d2[d])

        tot1 = tot//2
        tot = 0
        sq2 = 0
        for n in nums2:
            s = n*n
            for d in d1:
                if s%d == 0:
                    div = s//d
                    if div in d1:
                        if div == d:
                            sq2+=self.getCombo(d1[div])
                        else:
                            tot+=(d1[div]*d1[d])
        tot2 = tot//2
        return tot1+tot2+sq1+sq2


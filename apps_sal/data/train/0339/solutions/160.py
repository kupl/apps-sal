class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1= collections.Counter(nums1)
        c2= collections.Counter(nums2)
        r=0
        for n in nums1:
            for a in nums2:
                t = n*n//a

                if t*a == n*n:
                  
                    if t== a:
                        r= r+ (c2[t]-1)/2
                    else:
                        r= r+ c2[t]/2
        for a in nums1:
            for n in nums2:
                t= n*n//a
                if t*a == n*n:
                    if t== a:
                        r= r+ (c1[t]-1)/2
                    else:
                        r= r+ c1[t]/2
        return math.floor(r)
        
        
                        
                        
                            
                            


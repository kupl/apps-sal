class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(l1, l2):
            d = {}
            for c in l1:
                if c**2 in d:
                    d[c**2] += 1
                else:
                    d[c**2] = 1
            
            r = {}
            for c in l2:
                if c in r:
                    r[c] += 1
                else:
                    r[c] = 1
                    
            count = 0   
            for c in l2:
                for s in d:
                    res, c2 = s%c, s//c
                    if res == 0 and c2 in r:
                        if c2 != c:
                            count += r[c2] * d[s]
                        else:
                            count += (r[c2]-1) * d[s]
            return count//2
        
        return helper(nums1, nums2) + helper(nums2,nums1)

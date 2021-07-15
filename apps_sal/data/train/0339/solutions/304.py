class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = Counter(nums1)
        set2 = Counter(nums2)
        N1 = len(nums1)
        N2 = len(nums2)
        n1sq = [n*n for n in nums1]
        n2sq = [n*n for n in nums2]
        ntr = 0
        for i1 in range(N1): 
            for i2 in range(N2): 
                if n1sq[i1] % nums2[i2] == 0: 
                    if nums1[i1] != nums2[i2] and (n1sq[i1]//nums2[i2]) in set2: 
                        ntr += 0.5*set2[n1sq[i1]//nums2[i2]]
                    elif nums1[i1] == nums2[i2]: 
                        ntr += 0.5*(set2[nums2[i2]] - 1)
                if n2sq[i2] % nums1[i1] == 0: 
                    if nums2[i2] != nums1[i1] and (n2sq[i2]//nums1[i1]) in set1: 
                        ntr += 0.5*set1[n2sq[i2]//nums1[i1]]
                    elif nums2[i2] == nums1[i1]: 
                        ntr += 0.5*(set1[nums1[i1]]-1)
        return round(ntr)
        


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        totalcount=0
        nums1sq = defaultdict(int)
        for sq_val in [x*x for x in nums1]:
            nums1sq[sq_val]+=1
        nums2sq = defaultdict(int)
        for sq_val in [x*x for x in nums2]:
            nums2sq[sq_val]+=1
        #count type1
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                totalcount+=nums1sq[nums2[i]*nums2[j]]
        #count type2
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                totalcount+=nums2sq[nums1[i]*nums1[j]]
        return totalcount
                    
        


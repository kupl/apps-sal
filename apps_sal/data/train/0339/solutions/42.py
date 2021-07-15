class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        map1={}
        map2={}
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                prod=nums1[i]*nums1[j]
                map1.setdefault(prod,0)
                map1[prod]+=1
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                prod=nums2[i]*nums2[j]
                map2.setdefault(prod,0)
                map2[prod]+=1

        res=0
        for num in nums1:
            if num**2 in map2:
                res+=map2[num**2]
        for num in nums2:
            if num**2 in map1:
                res+=map1[num**2]
        return res


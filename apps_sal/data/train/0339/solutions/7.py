class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1=collections.defaultdict(int)
        d2=collections.defaultdict(int)
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                d1[nums1[i]*nums1[j]]+=1
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                d2[nums2[i]*nums2[j]]+=1
        c=0
        for i in nums1:
            c+=d2[i*i]
        for i in nums2:
            c+=d1[i*i]
        print(d1,d2)
        return c

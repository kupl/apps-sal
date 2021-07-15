class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter
        set1=Counter(nums1)
        set2=Counter(nums2)
        ret=0
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                temp=int(math.sqrt(nums1[i]*nums1[j]))
                if temp**2==nums1[i]*nums1[j] and temp in set2:
                    ret+=set2[temp]
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                temp=int(math.sqrt(nums2[i]*nums2[j]))
                if temp**2==nums2[i]*nums2[j] and temp in set1:
                    ret+=set1[temp]
        return ret

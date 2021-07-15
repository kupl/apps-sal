import collections
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        numsproddict=collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                numsproddict[nums1[i]*nums1[j]]+=1
        numsproddict2=collections.defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                numsproddict2[nums2[i]*nums2[j]]+=1
        ans=0
        for i in range(len(nums1)):
            ans+=numsproddict2[nums1[i]*nums1[i]]
        for i in range(len(nums2)):
            ans+=numsproddict[nums2[i]*nums2[i]]
        return ans

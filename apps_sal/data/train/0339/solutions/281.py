from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # nums2=sorted(nums2)
        # def isPresent(p, nums):
        #     start=0
        #     end=len(nums)-1
        #     while(start<end):
        def get_data(nums1,nums2):
            count=defaultdict(int)
            for i in range(len(nums2)):
                count[nums2[i]]+=1
            s=0
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if (nums1[i]*nums1[i])%nums2[j]!=0:
                        continue
                    elif nums2[j]==(nums1[i]*nums1[i])//nums2[j]:   
                        s+=(count[(nums1[i]*nums1[i])//nums2[j]]-1)
                    else:
                        s+=count[(nums1[i]*nums1[i])//nums2[j]]
            return s//2
        return get_data(nums1,nums2)+get_data(nums2, nums1)


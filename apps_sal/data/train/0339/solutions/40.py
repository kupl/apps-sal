class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1=[x*x for x in nums1]
        n2=[x*x for x in nums2]
        dnum1=collections.Counter(n1)
        dnum2=collections.Counter(n2)                
        ans=0
        nums1.sort()
        nums2.sort()
        m1=max(dnum1.keys())
        m2=max(dnum2.keys())
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                comb=nums1[i]*nums1[j]
                if comb in dnum2:
                    ans+=dnum2[nums1[i]*nums1[j]]
                if comb>m2:
                    break
               
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                comb=nums2[i]*nums2[j]
                if comb in dnum1:
                    ans+=dnum1[nums2[i]*nums2[j]]
                if comb>m1:
                    break
        return ans

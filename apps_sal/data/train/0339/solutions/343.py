class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        nn1 = []
        nn2 = []
        
        for j in range(n2):
            for k in range(j+1,n2):
                nn2.append(nums2[j]*nums2[k])
        for j in range(n1):
            for k in range(j+1,n1):
                nn1.append(nums1[j]*nums1[k])
        
        cnt = 0
        nnn1 = set(nums1)
        nnn2 = set(nums2)
        for i in nnn1:
            cnt+= nn2.count(i*i)*nums1.count(i)
        
        for i in nnn2:
            cnt+= nn1.count(i*i)*nums2.count(i)
        
        return cnt

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n1 = collections.Counter([num**2 for num in nums1])
        cnt = 0
        for i in range(1, len(nums2)):
            for j in range(i):
                if nums2[i]*nums2[j] in n1:
                    cnt += n1[nums2[i]*nums2[j]]
        
        n1 = collections.Counter([num**2 for num in nums2])
        for i in range(1, len(nums1)):
            for j in range(i):
                if nums1[i]*nums1[j] in n1:
                    cnt += n1[nums1[i]*nums1[j]]
        return cnt

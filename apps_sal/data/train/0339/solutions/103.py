class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m1, m2 = collections.Counter(), collections.Counter()
        
        result = 0
        
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                n = sqrt(nums1[i] * nums1[j])
                if n % 1 == 0:
                    m1[n] += 1
                
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                n = sqrt(nums2[i] * nums2[j])
                if n % 1 == 0:
                    m2[n] += 1
        
        for num in nums1:
            result += m2[num]
        for num in nums2:
            result += m1[num]
        return result

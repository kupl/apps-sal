class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = 0; b = 0
        i = 0; j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: a += nums1[i]; i+=1
            elif nums1[i] > nums2[j]: b += nums2[j]; j+=1
            else:
                a = b = max(a, b) + nums1[i];
                i+=1; j+=1

        while i < len(nums1): a += nums1[i]; i+=1
        while j < len(nums2): b += nums2[j]; j+=1
        return max(a, b) % 1_000_000_007


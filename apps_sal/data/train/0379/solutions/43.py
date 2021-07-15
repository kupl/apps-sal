class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0
        mx1 = 0 
        mx2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                mx1 = mx2 = max(mx1, mx2) + nums1[p1]
                p1 += 1
                p2 += 1
            while p1 < len(nums1) and p2 < len(nums2) and nums1[p1] < nums2[p2]:
                mx1 += nums1[p1]
                p1 += 1
            while p1 < len(nums1) and p2 < len(nums2) and nums2[p2] < nums1[p1]:
                mx2 += nums2[p2]
                p2 += 1
            
        while p1 < len(nums1):
            mx1 += nums1[p1]
            p1 += 1
        while p2 < len(nums2):
            mx2 += nums2[p2]
            p2 += 1
        return max(mx1,mx2) % (10**9+7)

class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        one = 0
        two = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                one = two = max(one, two) + nums1[i]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                two += nums2[j]
                j += 1
            else:
                one += nums1[i]
                i += 1
        while i < len(nums1):
            one += nums1[i]
            i += 1
        while j < len(nums2):
            two += nums2[j]
            j += 1
        return max(one, two) % 1000000007

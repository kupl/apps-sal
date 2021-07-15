class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        s1 = 0
        s2 = 0
        total = 0
        # [2 4 5 8 10]
        # [4 6 8 9]
        l1 = len(nums1)
        l2 = len(nums2)
        while s1 < l1 and s2 < l2:
            if nums1[s1] < nums2[s2]:
                sum1 += nums1[s1]
                s1 += 1
            elif nums1[s1] > nums2[s2]:
                sum2 += nums2[s2]
                s2 += 1
            else:
                total += max(sum1, sum2) + nums1[s1]
                sum1 = sum2 = 0
                s1 += 1
                s2 += 1
        if s1 < l1:
            while s1 < l1:
                sum1 += nums1[s1]
                s1 += 1
            total += max(sum1, sum2)
        if s2 < l2:
            while s2 < l2:
                sum2 += nums2[s2]
                s2 += 1
            total += max(sum1, sum2)
        return total % ((10 ** 9) + 7)

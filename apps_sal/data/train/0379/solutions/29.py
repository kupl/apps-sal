class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        score = 0
        total1 = 0
        total2 = 0
        pos1 = 0
        pos2 = 0

        while pos1 < len(nums1) or pos2 < len(nums2):
            if pos1 < len(nums1) and (pos2 >= len(nums2) or nums1[pos1] < nums2[pos2]):
                total1 += nums1[pos1]
                pos1 += 1
                continue

            if pos2 < len(nums2) and (pos1 >= len(nums1) or nums1[pos1] > nums2[pos2]):
                total2 += nums2[pos2]
                pos2 += 1
                continue

            score += nums1[pos1] + max(total1, total2)

            pos1 += 1
            pos2 += 1
            total1 = 0
            total2 = 0

        score += max(total1, total2)

        return score % (10**9 + 7)

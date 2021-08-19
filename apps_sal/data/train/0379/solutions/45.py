class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (sum1, sum2) = (0, 0)
        (index1, index2) = (0, 0)
        (len1, len2) = (len(nums1), len(nums2))
        while index1 < len1 or index2 < len2:
            if index1 < len1 and (index2 == len2 or nums1[index1] < nums2[index2]):
                sum1 += nums1[index1]
                index1 += 1
            elif index2 < len2 and (index1 == len1 or nums1[index1] > nums2[index2]):
                sum2 += nums2[index2]
                index2 += 1
            else:
                sum1 = sum2 = max(sum1, sum2) + nums1[index1]
                index1 += 1
                index2 += 1
        return max(sum1, sum2) % (10 ** 9 + 7)

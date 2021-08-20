class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        accu1 = list(accumulate(nums1))
        accu2 = list(accumulate(nums2))
        ans = i = j = 0
        pi = pj = -1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans += max(accu1[i], accu2[j]) if pi < 0 else max(accu1[i] - accu1[pi], accu2[j] - accu2[pj])
                (pi, pj, i, j) = (i, j, i + 1, j + 1)
        ans += max(accu1[-1], accu2[-1]) if pi < 0 else max(accu1[-1] - accu1[pi], accu2[-1] - accu2[pj])
        return ans % (10 ** 9 + 7)

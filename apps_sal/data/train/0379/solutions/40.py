class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dp1 = [0] * (len(nums1) + 1)
        dp2 = [0] * (len(nums2) + 1)

        dp1[-1] = 0
        dp2[-1] = 0

        to1 = {}
        to2 = {}
        inds2 = {y: j for j, y in enumerate(nums2)}
        for i, x in enumerate(nums1):
            if x in inds2:
                to2[i] = inds2[x]
                to1[inds2[x]] = i

        # print(dp1, dp2, to2, to1)

        i = len(nums1) - 1
        j = len(nums2) - 1

        while i >= 0 and j >= 0:
            if i not in to2:
                dp1[i] = nums1[i] + dp1[i + 1]
                i -= 1
            elif j not in to1:
                dp2[j] = nums2[j] + dp2[j + 1]
                j -= 1
            else:
                dp1[i] = dp2[j] = nums1[i] + max(dp1[i + 1], dp2[j + 1])
                i -= 1
                j -= 1

        # print(dp1, dp2)
        while i >= 0:
            dp1[i] = nums1[i] + dp1[i + 1]
            i -= 1

        while j >= 0:
            dp2[j] = nums2[j] + dp2[j + 1]
            j -= 1

        # print(dp1, dp2)

        return max(dp1[0], dp2[0]) % (10**9 + 7)

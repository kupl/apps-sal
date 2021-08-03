class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        def getSum(i, nums1, j, nums2):
            total = 0
            while (i < len(nums1)):
                total += nums1[i]
                i += 1
                while (i < len(nums1) and j < len(nums2) and nums2[j] < nums1[i]):
                    j += 1

                if i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                    if nums1[i] not in dp:
                        dp[nums1[i]] = max(getSum(i, nums1, j, nums2), getSum(j, nums2, i, nums1))
                    return total + dp[nums1[i]]

            return total

        dp = {}
        return max(getSum(0, nums1, 0, nums2), getSum(0, nums2, 0, nums1)) % (10**9 + 7)

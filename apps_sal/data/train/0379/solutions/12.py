class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(set(nums2))
        ans = 0
        segments1 = [0] * (len(common) + 1)

        tmp = 0
        j = 0
        for i in nums1:
            tmp += i
            if i in common:
                segments1[j] = tmp
                j += 1
                tmp = 0
        segments1[j] = tmp

        j = 0
        tmp = 0
        for i in nums2:
            tmp += i
            if i in common:
                ans += max(segments1[j], tmp)
                j += 1
                tmp = 0

        ans += max(segments1[j], tmp)

        return ans % (10**9 + 7)

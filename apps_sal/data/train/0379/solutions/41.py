MOD = 1000000007


class Solution:
    def maxSum(self, nums1, nums2):
        sum1, sum2, res = 0, 0, 0
        p1, p2 = 0, 0
        while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
            if nums1[p1] == nums2[p2]:
                res += max(sum1, sum2) + nums1[p1]
                sum1, sum2 = 0, 0
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                sum1 += nums1[p1]
                p1 += 1
            else:
                sum2 += nums2[p2]
                p2 += 1
        if p1 <= len(nums1) - 1:
            sum1 += sum(nums1[p1:])
        if p2 <= len(nums2) - 1:
            sum2 += sum(nums2[p2:])
        return (res + max(sum1, sum2)) % MOD

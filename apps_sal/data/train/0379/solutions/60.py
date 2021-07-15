MOD = 1000000007
class Solution:
    def maxSum(self, nums1, nums2):
        sum1, sum2, res = 0, 0, 0
        p1, p2 = 0, 0
        while p1 <= len(nums1) - 1 or p2 <= len(nums2) - 1:
            if p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1 and nums1[p1] == nums2[p2]:
                res = (res + max(sum1, sum2) + nums1[p1]) % MOD
                sum1, sum2 = 0, 0
                p1 += 1
                p2 += 1
            elif p2 > len(nums2) - 1 or (p1 <= len(nums1) - 1 and nums1[p1] < nums2[p2]):
                sum1 = sum1 + nums1[p1]
                p1 += 1
            else:
                sum2 = sum2 + nums2[p2]
                p2 += 1

        return (res + max(sum1, sum2)) % MOD

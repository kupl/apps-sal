class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if all(x >= 0 for x in nums1) and all(y <= 0 for y in nums2):
            return min(nums1) * max(nums2)
        if all(x <= 0 for x in nums1) and all(y >= 0 for y in nums2):
            return max(nums1) * min(nums2)
        accu_max = [0] * (len(nums2) + 1)
        for i in range(len(nums1)):
            last_max = [accu_max[j] + nums1[i] * nums2[j] for j in range(len(nums2))]
            this_accu_max = [0]
            for j in range(len(nums2)):
                this_accu_max.append(max(this_accu_max[-1], last_max[j], accu_max[j + 1]))
            accu_max = this_accu_max
        return accu_max[-1]

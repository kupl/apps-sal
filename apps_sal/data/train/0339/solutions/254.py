from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1, c2 = Counter(nums1), Counter(nums2)
        n, m = len(nums1), len(nums2)
        ans = 0
        for i in range(n):
            for j in range(m):
                nums2_k = (nums1[i] * nums1[i]) / nums2[j]
                ans += c2[nums2_k]
                if nums2_k == nums2[j]:
                    ans -= 1

        for i in range(m):
            for j in range(n):
                nums1_k = (nums2[i] * nums2[i]) / nums1[j]
                ans += c1[nums1_k]
                if nums1_k == nums1[j]:
                    ans -= 1

        return ans // 2

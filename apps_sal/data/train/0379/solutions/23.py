class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        cross = []
        (n, m) = (len(nums1), len(nums2))
        (i, j) = (0, 0)
        M = 10 ** 9 + 7
        while i < n and j < m:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums2[j] > nums1[i]:
                i += 1
            else:
                cross.append((i, j))
                i += 1
                j += 1
        l = len(cross)
        if l == 0:
            return max(sum(nums1), sum(nums2)) % M
        ans = max(sum(nums1[cross[-1][0]:]), sum(nums2[cross[-1][1]:]))
        ans %= M
        for i in range(l - 2, -1, -1):
            ans += max(sum(nums1[cross[i][0]:cross[i + 1][0]]), sum(nums2[cross[i][1]:cross[i + 1][1]]))
            ans %= M
        ans += max(sum(nums1[:cross[0][0]]), sum(nums2[:cross[0][1]]))
        ans %= M
        return ans % M

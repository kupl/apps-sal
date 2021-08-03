class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.num1_idx = {x: i for i, x in enumerate(nums1)}
        self.num2_idx = {x: i for i, x in enumerate(nums2)}
        self.memo = {}
        s1 = self.helper(nums1, nums2, nums1[0])
        s2 = self.helper(nums1, nums2, nums2[0])
        return max(s1, s2) % (10**9 + 7)

    def helper(self, nums1, nums2, val):
        if val in self.memo:
            return self.memo[val]

        ans1, ans2 = 0, 0
        if val in self.num1_idx:
            idx = self.num1_idx[val]
            if idx + 1 < len(nums1):
                ans1 = self.helper(nums1, nums2, nums1[idx + 1])

        if val in self.num2_idx:
            idx = self.num2_idx[val]
            if idx + 1 < len(nums2):
                ans2 = self.helper(nums1, nums2, nums2[idx + 1])

        res = max(ans1, ans2) + val
        self.memo[val] = res
        return res

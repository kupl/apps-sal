class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        def helper(l1, l2):
            nonlocal ans
            for e in l1:
                tar = e**2
                dp = Counter()
                for x in l2:
                    if tar % x == 0:
                        ans += dp[tar // x]
                    dp[x] += 1
        helper(nums1, nums2)
        helper(nums2, nums1)
        return ans

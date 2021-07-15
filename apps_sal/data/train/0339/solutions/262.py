class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def helper(l1, l2):
            ans = 0
            for e in l1:
                dp = Counter()
                tar = e**2
                for x in l2:
                    if tar%x == 0:
                        ans += dp[tar//x]
                    dp[x] += 1
            return ans
        
        return helper(nums1, nums2) + helper(nums2, nums1)

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        rev1 = {v:k for k, v in enumerate(nums1)}
        rev2 = {v:k for k, v in enumerate(nums2)}
        
        def dp(val, memo):
            if val in memo:
                return memo[val]
            ans = 0
            if val in rev1:
                ans = val
                if rev1[val] < len(nums1) -1:
                    ans = max(ans, dp(nums1[rev1[val] + 1], memo) + val)
            if val in rev2:
                ans = max(ans, val)
                if rev2[val] < len(nums2) -1:
                    ans = max(ans, dp(nums2[rev2[val] + 1], memo) + val)
            ans = ans
            memo[val] = ans
            return ans
        memo = {}
        return max(dp(nums1[0], memo), dp(nums2[0], memo)) %(1000000007)

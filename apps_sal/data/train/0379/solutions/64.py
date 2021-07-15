class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = nums1, nums2
        m, n = len(a), len(b)
        p1 = {x:i for i, x in enumerate(a)}
        p2 = {x:i for i, x in enumerate(b)}
        
        @lru_cache(None)
        def dp(i, use_a):
            if use_a:
                if i == m:
                    return 0
                ans = a[i] + dp(i + 1, True)
                if a[i] in p2:
                    j = p2[a[i]] + 1
                    ans = max(ans, a[i] + dp(j, False))
            else:
                if i == n:
                    return 0
                ans = b[i] + dp(i +1, False)
                if b[i] in p1:
                    j = p1[b[i]] + 1
                    ans = max(ans, b[i] + dp(j, True))
            return ans 
        
        return max(dp(0, True), dp(0, False)) % (10 ** 9 + 7)
                


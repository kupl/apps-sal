import numpy as np
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        # DP(a=index of last, b=index of last) = max of:
        #   DP(a-1, b)
        #   DP(a-1, i) + nums1[a] * max_or_min(nums2[i+1:b+1])
        #   same for b
        
        INF = int(1e9)
        n, m = len(nums1), len(nums2)

        DP = np.ones((n, m), dtype=int) * -INF
        DP[0, 0] = nums1[0] * nums2[0]
        
        for a in range(n):
            for b in range(m):
                
                el = nums1[a] * nums2[b]
                curr = el
                
                if a > 0:
                    curr = max(curr, DP[a - 1, b])
                if b > 0:
                    curr = max(curr, DP[a, b - 1])
                if a > 0 and b > 0:
                    prev = DP[a - 1, b - 1]
                    curr = max(curr, prev, prev + el)
                    
                DP[a, b] = curr
                    
        return DP[-1, -1]

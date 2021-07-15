from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(A, B):
            ans = 0
            C = Counter([a*a for a in A])
            D = Counter()
            for b in B:
                for k, v in D.items():
                    if k*b in C:
                        ans += v * C[k*b]
                D[b] += 1
            return ans
        
        return helper(nums1, nums2) + helper(nums2, nums1)

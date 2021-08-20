from collections import defaultdict


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def solv(A, B):
            ans = 0
            for a in A:
                x = a ** 2
                seen = defaultdict(lambda: 0)
                for b in B:
                    (q, r) = divmod(x, b)
                    if r != 0:
                        seen[b] += 1
                        continue
                    ans += seen[q]
                    seen[b] += 1
            return ans
        return solv(nums1, nums2) + solv(nums2, nums1)

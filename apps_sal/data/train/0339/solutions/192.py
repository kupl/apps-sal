class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            ret = 0
            C = collections.Counter(nums2)
            s = sorted(C)
            for n in nums1:
                ret += C[n] * (C[n] - 1) // 2
                nn = n * n
                for d in s:
                    if d >= n:
                        break
                    if nn % d == 0:
                        ret += C[d] * C[nn // d]
            return ret
        
        return helper(nums1, nums2) + helper(nums2, nums1)

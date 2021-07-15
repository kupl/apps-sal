from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dot(i, j):
            if i == N1 or j == N2: return -sys.maxsize
            ans = nums1[i]*nums2[j]
            ans = max(ans,
                      ans + dot(i + 1, j + 1),
                      dot(i, j + 1),
                      dot(i + 1, j),
                      dot(i + 1, j + 1)
                     )
            return ans
        N1, N2 = len(nums1), len(nums2)
        return dot(0, 0)

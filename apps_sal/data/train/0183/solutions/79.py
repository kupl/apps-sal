class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return dp_with_recursion(nums1, nums2)


def dp_with_recursion(a, b):
    @lru_cache(maxsize=None)
    def recursion(i, j, is_empty=True):
        if i < 0 or j < 0:
            return float('-inf') if is_empty else 0
        # BUG, BUG!
        # return max(recursion(i, j-1), recursion(i-1,j), recursion(i-1,j-1) + max(0, a[i]*b[j]))
        # return max(recursion(i, j-1), recursion(i-1,j), recursion(i-1, j-1, False) + a[i]*b[j])
        return max(recursion(i, j - 1, is_empty), recursion(i - 1, j, is_empty), recursion(i - 1, j - 1, False) + a[i] * b[j])
    return recursion(len(a) - 1, len(b) - 1)

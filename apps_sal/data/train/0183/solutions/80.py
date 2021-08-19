class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        a = [[-1 for _ in range(len(nums2))] for _ in range(len(nums1))]

        def dp(x, y):
            if len(nums1) == x or len(nums2) == y:
                return -float('inf')
            if a[x][y] != -1:
                return a[x][y]
            else:
                a[x][y] = max(dp(x + 1, y), dp(x, y + 1), dp(x + 1, y + 1) + nums1[x] * nums2[y], nums1[x] * nums2[y])
                return a[x][y]
        return dp(0, 0)

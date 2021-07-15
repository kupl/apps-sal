class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        d = [[0] * (n2+1) for _ in range(n1+1)]
        inf = -float('inf')
        for i in range(n1):
            for j in range(n2):
                d[i][j] = max(d[i-1][j] if i else inf,d[i][j-1] if j else inf, nums1[i] * nums2[j] + (d[i-1][j-1] if d[i-1][j-1] > 0 else 0))
        return d[n1-1][n2-1]

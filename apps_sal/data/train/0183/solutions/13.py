class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        M = [[-100000] * (n2 + 1)  for _ in range(n1 + 1)]

        for i in range(n1):
            for j in range(n2):
                M[i+1][j+1] = max(M[i][j]+nums1[i]*nums2[j], M[i][j+1], M[i+1][j], nums1[i]*nums2[j])
        return M[-1][-1]

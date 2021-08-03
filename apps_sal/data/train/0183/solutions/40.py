def max_dot_product(A, B):
    mem = {}
    for i in range(len(A)):
        for j in range(len(B)):
            if i == j == 0:
                ans = A[i] * B[j]
            elif i == 0:
                ans = max(A[i] * B[j], mem[i, j - 1])
            elif j == 0:
                ans = max(A[i] * B[j], mem[i - 1, j])
            else:
                ans = max(A[i] * B[j], A[i] * B[j] + mem[i - 1, j - 1], mem[i, j - 1], mem[i - 1, j])
            mem[i, j] = ans
    return mem[len(A) - 1, len(B) - 1]


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return max_dot_product(nums1, nums2)

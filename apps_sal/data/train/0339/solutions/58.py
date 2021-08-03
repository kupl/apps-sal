class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def check(A, B):
            n, res = len(B), 0
            C = Counter(map(lambda i: i * i, A))

            for i in range(n):
                for j in range(i + 1, n):
                    res += C[B[i] * B[j]]

            return res

        return check(nums1, nums2) + check(nums2, nums1)

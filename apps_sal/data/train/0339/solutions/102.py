from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def mults(arr, N):
            return Counter([arr[i] * arr[j] for i in range(N) for j in range(N) if i != j])

        def squares(arr):
            return list([x ** 2 for x in arr])
        count = 0
        (A, B) = (squares(nums1), mults(nums2, len(nums2)))
        (C, D) = (squares(nums2), mults(nums1, len(nums1)))
        for a in A:
            if a in B:
                count += B[a]
        for a in C:
            if a in D:
                count += D[a]
        return count // 2

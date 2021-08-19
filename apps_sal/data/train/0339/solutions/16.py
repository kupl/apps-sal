class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter((num * num for num in nums1))
        counter2 = Counter((num * num for num in nums2))
        res = 0
        (n, m) = (len(nums1), len(nums2))
        for i in range(n - 1):
            for j in range(i + 1, n):
                curr = nums1[i] * nums1[j]
                res += counter2[curr]
        for i in range(m - 1):
            for j in range(i + 1, m):
                curr = nums2[i] * nums2[j]
                res += counter1[curr]
        return res

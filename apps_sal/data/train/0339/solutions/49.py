class Solution:
    def helper(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0
        h1 = {}
        for j in range(n1):
            for k in range(j + 1, n1):
                if nums1[j] * nums1[k] not in h1:
                    h1[nums1[j] * nums1[k]] = 1
                else:
                    h1[nums1[j] * nums1[k]] += 1

        l = [i**2 for i in nums2]

        ans = 0
        for i in l:
            if i in h1:
                ans += h1[i]
        return ans

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        return self.helper(nums1, nums2) + self.helper(nums2, nums1)

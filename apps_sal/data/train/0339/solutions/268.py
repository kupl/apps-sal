class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums1.sort()
        nums2.sort()
        for i in range(len(nums2)):
            ii = nums2[i]**2
            ar = {}
            for j in range(len(nums1)):
                # print(nums1[j], ii, ar)
                if ii % nums1[j] == 0:
                    g = ii // nums1[j]
                else:
                    ar[nums1[j]] = ar.get(nums1[j], 0) + 1
                    continue

                # print(nums1[j], g, ii)
                if ar.get(g) is not None:
                    ans += ar[g]
                ar[nums1[j]] = ar.get(nums1[j], 0) + 1

        for i in range(len(nums1)):
            ii = nums1[i]**2
            ar = {}
            for j in range(len(nums2)):
                # print(nums2[j], ii, ar, nums2)
                if ii % nums2[j] == 0:
                    g = ii // nums2[j]
                else:
                    ar[nums2[j]] = ar.get(nums2[j], 0) + 1
                    continue

                # print(nums2[j], g, ii)
                if ar.get(g) is not None:
                    ans += ar[g]
                ar[nums2[j]] = ar.get(nums2[j], 0) + 1
        return ans

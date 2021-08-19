class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        ans = 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]
                if int(math.sqrt(p)) ** 2 == p and int(math.sqrt(p)) in d2:
                    ans += d2[int(math.sqrt(p))]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                p = nums2[i] * nums2[j]
                if int(math.sqrt(p)) ** 2 == p and int(math.sqrt(p)) in d1:
                    ans += d1[int(math.sqrt(p))]
        return ans

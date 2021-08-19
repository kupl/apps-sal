from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        da = Counter(nums1)
        db = Counter(nums2)
        cnt = 0
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                p = nums2[i] * nums2[j]
                if math.isqrt(p) ** 2 == p and math.isqrt(p) in da:
                    cnt += da[int(math.sqrt(p))]
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]
                if math.isqrt(p) ** 2 == p and math.isqrt(p) in db:
                    cnt += db[int(math.sqrt(p))]
        return cnt

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        prod2 = collections.defaultdict(int)

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                prod = nums2[i] * nums2[j]

                if prod in prod2:
                    prod2[prod] += 1
                else:
                    prod2[prod] = 1

        res = 0

        for e in nums1:

            if e**2 in prod2:
                res += prod2[e**2]

        prod1 = collections.defaultdict(int)

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                prod = nums1[i] * nums1[j]

                if prod in prod1:
                    prod1[prod] += 1
                else:
                    prod1[prod] = 1

        for e in nums2:
            if e * e in prod1:
                res += prod1[e * e]

        return res

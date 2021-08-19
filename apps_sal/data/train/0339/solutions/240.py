class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def twoProduct(list1, list2, target):
            res = 0
            counter = collections.defaultdict(int)
            for j in range(len(list2)):
                (q, r) = divmod(target, list2[j])
                if r == 0 and q in counter:
                    res += counter[q]
                counter[list2[j]] += 1
            return res
        res = 0
        for n in nums1:
            res += twoProduct(nums1, nums2, n ** 2)
        for n in nums2:
            res += twoProduct(nums2, nums1, n ** 2)
        return res

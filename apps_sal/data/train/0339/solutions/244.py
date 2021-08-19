class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        # type1
        d1 = collections.defaultdict(int)
        l1 = [i**2 for i in nums1]
        for i in range(len(nums2)):
            if nums2[i] in d1:
                res += d1[nums2[i]]
            for j in range(len(l1)):
                if l1[j] % nums2[i] == 0:
                    d1[l1[j] // nums2[i]] += 1
        d2 = collections.defaultdict(int)
        l2 = [i**2 for i in nums2]
        for i in range(len(nums1)):
            if nums1[i] in d2:
                res += d2[nums1[i]]
            for j in range(len(l2)):
                if l2[j] % nums1[i] == 0:
                    d2[l2[j] // nums1[i]] += 1

        return res

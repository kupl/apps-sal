class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        d1 = collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                sqr = math.sqrt(nums1[i] * nums1[j])
                if sqr == int(sqr):
                    d1[int(sqr)] += 1
        for i in nums2:
            if i in d1:
                res += d1[i]
        d2 = collections.defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                sqr = math.sqrt(nums2[i] * nums2[j])
                if sqr == int(sqr):
                    d2[int(sqr)] += 1
        for i in nums1:
            if i in d2:
                res += d2[i]
        return res

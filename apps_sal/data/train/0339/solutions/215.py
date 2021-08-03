class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = defaultdict(list)
        d2 = defaultdict(list)

        for i, x in enumerate(nums1):
            for j, y in enumerate(nums1):
                if j <= i:
                    continue
                r = int(sqrt(x * y))
                if r**2 == x * y:
                    d1[r].append((i, j))

        for i, x in enumerate(nums2):
            for j, y in enumerate(nums2):
                if j <= i:
                    continue
                r = int(sqrt(x * y))
                if r**2 == x * y:
                    d2[r].append((i, j))
        ret = 0
        for i in nums1:
            ret += len(d2[i])
        for i in nums2:
            ret += len(d1[i])

        return ret

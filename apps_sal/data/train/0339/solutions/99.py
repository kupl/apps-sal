class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        hh = defaultdict(int)
        nums1.sort()
        for (m, i) in enumerate(nums1):
            hh[i * i] += 1
        h = defaultdict(int)
        for i in nums2:
            h[i] += 1
        r = 0
        print(h)
        for i in h:
            for j in h:
                if i <= j and i * j in hh:
                    if i == j:
                        r += h[i] * (h[i] - 1) // 2 * hh[i * j]
                    else:
                        r += h[i] * h[j] * hh[i * j]
        (nums1, nums2) = (nums2, nums1)
        hh = defaultdict(int)
        nums1.sort()
        for (m, i) in enumerate(nums1):
            hh[i * i] += 1
        h = defaultdict(int)
        for i in nums2:
            h[i] += 1
        print(h)
        for i in h:
            for j in h:
                if i <= j and i * j in hh:
                    if i == j:
                        r += h[i] * (h[i] - 1) // 2 * hh[i * j]
                    else:
                        r += h[i] * h[j] * hh[i * j]
        return r

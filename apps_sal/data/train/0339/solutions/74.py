class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        m = len(nums2)
        n2dict = defaultdict(int)
        m2dict = defaultdict(int)
        for x in nums1:
            n2dict[x * x] += 1
        for x in nums2:
            m2dict[x * x] += 1
        out = 0

        for i in range(m):
            for j in range(i + 1, m):
                key = nums2[i] * nums2[j]
                if nums2[i] * nums2[j] in n2dict:
                    out += (n2dict[key])

        for i in range(n):
            for j in range(i + 1, n):
                key = nums1[i] * nums1[j]

                if key in m2dict:
                    out += (m2dict[key])

        return out

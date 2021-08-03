import bisect


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        v2i1, v2i2 = dict(), dict()
        n1, n2 = len(nums1), len(nums2)
        for i in range(0, n1):
            if not nums1[i] in v2i1:
                v2i1[nums1[i]] = []
            v2i1[nums1[i]].append(i)

        for i in range(0, n2):
            if not nums2[i] in v2i2:
                v2i2[nums2[i]] = []
            v2i2[nums2[i]].append(i)

        result = 0

        for z in nums1:
            z = z * z
            for x in v2i2:
                if (z % x) == 0 and (z // x) in v2i2:
                    y = z // x
                    if y != x:
                        js, ks = v2i2[x], v2i2[y]
                        for j in js:
                            k = bisect.bisect_left(ks, j)
                            result += len(ks) - k
                    else:
                        result += len(v2i2[x]) * (len(v2i2[x]) - 1) // 2
        for z in nums2:
            z = z * z
            for x in v2i1:
                if (z % x) == 0 and (z // x) in v2i1:
                    y = z // x
                    if y != x:
                        js, ks = v2i1[x], v2i1[y]
                        for j in js:
                            k = bisect.bisect_left(ks, j)
                            result += len(ks) - k
                    else:
                        result += len(v2i1[x]) * (len(v2i1[x]) - 1) // 2
        return result

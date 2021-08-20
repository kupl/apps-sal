class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        dic1 = {}
        dic2 = {}
        for x in nums1:
            if x not in dic1:
                dic1[x] = 0
            dic1[x] += 1
        for x in nums2:
            if x not in dic2:
                dic2[x] = 0
            dic2[x] += 1
        for (k, v) in dic1.items():
            for (k1, v1) in dic2.items():
                if k1 < k:
                    if k ** 2 % k1 == 0:
                        if k ** 2 / k1 in dic2:
                            result += v * v1 * dic2[k ** 2 / k1]
                elif k1 == k:
                    result += v * v1 * (v1 - 1) / 2
        for (k, v) in dic2.items():
            for (k1, v1) in dic1.items():
                if k1 < k:
                    if k ** 2 % k1 == 0:
                        if k ** 2 / k1 in dic1:
                            result += v * v1 * dic1[k ** 2 / k1]
                elif k1 == k:
                    result += v * v1 * (v1 - 1) / 2
        return int(result)

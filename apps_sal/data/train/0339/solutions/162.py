class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = {}
        d2 = {}
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        count = 0
        for key in d1:
            for x in d2:
                if key ** 2 % x == 0:
                    if key ** 2 // x == x:
                        if d2[x] > 1:
                            count += d1[key] * (d2[x] - 1) * d2[x]
                    elif key ** 2 // x in d2:
                        count += d1[key] * d2[x] * d2[key ** 2 // x]
        for key in d2:
            for x in d1:
                if key ** 2 % x == 0:
                    if key ** 2 // x == x:
                        if d1[x] > 1:
                            count += d2[key] * (d1[x] - 1) * d1[x]
                    elif key ** 2 // x in d1:
                        count += d2[key] * d1[x] * d1[key ** 2 // x]
        return count // 2

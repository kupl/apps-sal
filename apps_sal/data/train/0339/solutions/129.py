class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        dict1 = dict()
        dict2 = dict()
        for x in nums1:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        for x in nums2:
            if x in dict2:
                dict2[x] += 1
            else:
                dict2[x] = 1
        for x in nums1:
            squar = x**2
            for y in nums2:
                if (squar / y) in dict2:
                    if (squar / y) == y:
                        result += dict2[squar / y] - 1
                    else:
                        result += dict2[squar / y]
        for x in nums2:
            squar = x**2
            for y in nums1:
                if (squar / y) in dict1:
                    if (squar / y) == y:
                        result += dict1[squar / y] - 1
                    else:
                        result += dict1[squar / y]
        return int(result / 2)

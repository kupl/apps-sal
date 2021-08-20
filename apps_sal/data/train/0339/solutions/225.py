class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums1square = []
        for i in nums1:
            nums1square.append(i * i)
        for i in nums1square:
            d = dict()
            for j in nums2:
                if i % j == 0:
                    if i / j in d.keys():
                        ans += d[i / j]
                    if j in d.keys():
                        d[j] += 1
                    else:
                        d[j] = 1
        nums2square = []
        for i in nums2:
            nums2square.append(i * i)
        for i in nums2square:
            d = dict()
            for j in nums1:
                if i % j == 0:
                    if i / j in d.keys():
                        ans += d[i / j]
                    if j in d.keys():
                        d[j] += 1
                    else:
                        d[j] = 1
        return ans

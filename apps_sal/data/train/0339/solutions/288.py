class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import defaultdict
        import math
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for k in range(len(nums1) - 1):
            for j in range(k + 1, len(nums1)):
                temp = nums1[k] * nums1[j]
                if temp - math.ceil(temp ** 0.5) ** 2 == 0:
                    cnt1[temp] += 1
        for k in range(len(nums2) - 1):
            for j in range(k + 1, len(nums2)):
                temp = nums2[k] * nums2[j]
                if temp - math.ceil(temp ** 0.5) ** 2 == 0:
                    cnt2[temp] += 1
        print(cnt1, cnt2)
        res = 0
        for t in nums1:
            res += cnt2[t ** 2]
        for t in nums2:
            res += cnt1[t ** 2]
        return res
        return res

class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (ind1, ind2) = (defaultdict(list), defaultdict(list))
        for (i, v) in enumerate(nums1):
            ind1[v].append(i)
        for (i, v) in enumerate(nums2):
            ind2[v].append(i)
        (type1, type2) = (0, 0)
        for (i, v) in enumerate(nums1):
            for (j, v2) in enumerate(nums2):
                if v * v % v2:
                    continue
                req = v * v // v2
                type1 += len(ind2[req]) - (v2 == req)
        for (i, v) in enumerate(nums2):
            for v1 in nums1:
                if v * v % v1:
                    continue
                req = v * v // v1
                type2 += len(ind1[req]) - (v1 == req)
        print(type1, type2)
        ans = type1 // 2 + type2 // 2
        return ans

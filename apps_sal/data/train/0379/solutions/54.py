class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        H1 = {}
        H2 = {}
        for i in range(len(nums1)):
            H1[nums1[i]] = i
        for i in range(len(nums2)):
            H2[nums2[i]] = i
        S1 = set(H1.keys())
        S2 = set(H2.keys())
        C = sorted(list(S1.intersection(S2)))
        if len(C) == 0:
            return max(sum(nums1), sum(nums2))
        ind1 = ind2 = 0
        n1 = []
        n2 = []
        n = 0
        for i in C:
            i1 = H1[i] + 1
            i2 = H2[i] + 1
            n += max(sum(nums1[ind1:i1]), sum(nums2[ind2:i2]))
            n1.append(sum(nums1[ind1:H1[i] + 1]))
            n2.append(sum(nums2[ind2:H2[i] + 1]))
            ind1 = H1[i] + 1
            ind2 = H2[i] + 1
        n1.append(sum(nums1[ind1:]))
        n2.append(sum(nums2[ind2:]))
        n += max(sum(nums1[ind1:]), sum(nums2[ind2:]))
        return n % 1000000007

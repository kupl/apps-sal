class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def typeone(n1, n2):
            L1 = len(n1)
            L2 = len(n2)
            dic = {}
            count = 0
            for j in range(L2 - 1):
                for k in range(j + 1, L2):
                    if n2[j] * n2[k] not in dic:
                        dic[n2[j] * n2[k]] = 1
                    else:
                        dic[n2[j] * n2[k]] += 1
            for u in n1:
                if u * u in dic:
                    count += dic[u * u]
            return count
        return typeone(nums1, nums2) + typeone(nums2, nums1)

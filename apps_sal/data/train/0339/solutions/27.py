class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def cal(lst1, lst2):
            count = 0
            d = {}
            for i in range(len(lst1)):
                v = lst1[i] * lst1[i]
                d[v] = d.get(v, 0) + 1
            for j in range(len(lst2)):
                for k in range(j + 1, len(lst2)):
                    v = lst2[j] * lst2[k]
                    if v in d:
                        count += d[v]
            return count
        return cal(nums1, nums2) + cal(nums2, nums1)

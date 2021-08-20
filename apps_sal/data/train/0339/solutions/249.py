class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        tmp_dict1 = dict()
        res = 0
        for (i, v) in enumerate(nums1):
            if v not in tmp_dict1:
                tmp_dict1[v] = self.get_num_tr(v, nums2)
            res += tmp_dict1.get(v)
        tmp_dict2 = dict()
        for (i, v) in enumerate(nums2):
            if v not in tmp_dict2:
                tmp_dict2[v] = self.get_num_tr(v, nums1)
            res += tmp_dict2.get(v)
        return res

    def get_num_tr(self, num, nums):
        n = num * num
        res = 0
        dct = dict()
        for (i, v) in enumerate(nums):
            if n % v == 0:
                res += dct.get(int(n / v), 0)
            dct[v] = dct.get(v, 0) + 1
        return res

class Solution:

    def all_products(self, int_list):
        res_list = []
        for idx, i in enumerate(int_list):
            for j in int_list[idx + 1:]:
                res_list.append(i * j)
        return res_list

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        squared_nums1 = [i**2 for i in nums1]
        squared_nums2 = [i**2 for i in nums2]
        products_nums1 = self.all_products(nums1)
        products_nums2 = self.all_products(nums2)
        for i in set(squared_nums2):
            c1 = squared_nums2.count(i)
            c2 = products_nums1.count(i)
            res += c1 * c2
        for j in set(squared_nums1):
            d1 = squared_nums1.count(j)
            d2 = products_nums2.count(j)
            res += d1 * d2
        return res

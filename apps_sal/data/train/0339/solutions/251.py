class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def get_prod_dic(arr, num_dic):
            i = 0
            while i < len(arr):
                j = i + 1
                while j < len(arr):
                    p = arr[i] * arr[j]
                    if p not in num_dic:
                        num_dic[p] = []
                    num_dic[p].append([i, j])
                    j += 1
                i += 1
            return
        n1_dic = {}
        get_prod_dic(nums1, n1_dic)
        n2_dic = {}
        get_prod_dic(nums2, n2_dic)
        count = 0
        for n in nums1:
            p = n * n
            if p in n2_dic:
                count += len(n2_dic[p])
        for n in nums2:
            p = n * n
            if p in n1_dic:
                count += len(n1_dic[p])
        return count

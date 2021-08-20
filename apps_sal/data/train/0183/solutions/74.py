class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {}
        dic[0, 0] = nums1[0] * nums2[0]

        def search(i, j):
            a = nums1[i] * nums2[j]
            if (i, j) in dic:
                return dic[i, j]
            if i == 0:
                dic[0, j] = max(search(0, j - 1), a)
                return dic[i, j]
            elif j == 0:
                dic[i, 0] = max(search(i - 1, 0), a)
                return dic[i, 0]
            else:
                dic[i, j] = max(search(i - 1, j), search(i, j - 1), a + search(i - 1, j - 1), a)
                return dic[i, j]
        return search(len(nums1) - 1, len(nums2) - 1)

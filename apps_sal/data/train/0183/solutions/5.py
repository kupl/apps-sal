class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        def dp(nums1, nums2, i, j, m, n, dic):
            if i + 1 >= m:
                maximum = None
                for p in range(j, n):
                    if maximum == None:
                        maximum = nums1[i] * nums2[p]
                    else:
                        maximum = max(maximum, nums1[i] * nums2[p])
                return maximum
            elif j + 1 >= n:
                maximum = None
                for p in range(i, m):
                    if maximum == None:
                        maximum = nums1[p] * nums2[j]
                    else:
                        maximum = max(maximum, nums1[p] * nums2[j])
                return maximum
            if dic[i][j] != None:
                return dic[i][j]
            dic[i][j] = max(nums1[i] * nums2[j], nums1[i] * nums2[j] + dp(nums1, nums2, i + 1, j + 1, m, n, dic), dp(nums1, nums2, i, j + 1, m, n, dic), dp(nums1, nums2, i + 1, j, m, n, dic), dp(nums1, nums2, i + 1, j + 1, m, n, dic))
            return dic[i][j]
        dic = []
        m = len(nums1)
        n = len(nums2)
        for i in range(m):
            dic.append([None] * n)
        return dp(nums1, nums2, 0, 0, m, n, dic)

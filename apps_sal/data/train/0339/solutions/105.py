class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        mat2 = [[0 for i in range(n)] for i in range(n)]

        def fillUpper(m, nums):
            mat = [[0 for i in range(m)] for i in range(m)]
            mapp1 = defaultdict(int)
            for i in range(m - 1):
                for j in range(i + 1, len(mat)):
                    # mat[i][j] = nums[i]**2 + nums[j]**2
                    mapp1[nums[i] * nums[j]] += 1

            return mapp1
        mat1 = fillUpper(m, nums1)
        mat2 = fillUpper(n, nums2)
        res = 0
        for i in nums1:
            c = i**2
            if(c in mat2):
                res += mat2[c]
        for i in nums2:
            c = i**2
            if(c in mat1):
                res += mat1[c]
        return res

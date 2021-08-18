class Solution:
    def maxDotProduct(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        mem = [[None] * n for i in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mem[i][j] = nums1[i] * nums2[j]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                max_ = mem[i + 1][j + 1] if i + 1 < m and j + 1 < n else -1001
                mem[i][j] = max(mem[i][j] + max_, max(mem[i][j], max_))
                mem[i][j] = max(mem[i][j],
                                mem[i][j + 1] if j < n - 1 else -1001)
                mem[i][j] = max(mem[i][j],
                                mem[i + 1][j] if i < m - 1 else -1001)
        return mem[0][0]

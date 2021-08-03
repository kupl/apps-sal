class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        mem = [[float('-inf')] * (n2 + 1) for _ in range(n1 + 1)]
        mem[0][0] = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                mem[i][j] = max(mem[i][j], max(nums1[i - 1] * nums2[j - 1] + max(0, mem[i - 1][j - 1]), mem[i][j - 1], mem[i - 1][j]))
        # print(mem)
        return mem[n1][n2]

        # mem = [[[[float('-inf')] * n2 for j in range(n2)] for i1 in range(n1)] for i2 in range(n1)]
        @lru_cache
        def dp(i1, j1, i2, j2):
            if i1 > j1 or i2 > j2:
                return 0
            if i1 == j1 and i2 == j2:
                return nums1[i1] * nums2[i2]
            if mem[i1][j1][i2][j2] != float('-inf'):
                return mem[i1][j1][i2][j2]
            ans = float('-inf')
            for k1 in range(i1, j1 + 1):
                for k2 in range(i2, j2 + 1):
                    ans = max(ans, max(0, nums1[k1] * nums2[k2]) + dp(i1, k1 - 1, i2, k2 - 1) + dp(k1 + 1, j1, k2 + 1, j2))
            mem[i1][j1][i2][j2] = ans
            return ans

        return dp(0, n1 - 1, 0, n2 - 1)

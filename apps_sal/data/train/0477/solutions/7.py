class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        l = [0] * (n + 1)
        for i in range(1, n + 1):
            l[i] = 2 * l[i - 1] + 1

        def helper(n, k, f):
            m = l[n]
            if n == 1:
                return 0 ^ f
            if k == m // 2 + 1:
                return 1 ^ f
            if k <= m // 2:
                return helper(n - 1, k, f)
            else:
                return helper(n - 1, m - k + 1, 1 ^ f)
        return str(helper(n, k, 0))

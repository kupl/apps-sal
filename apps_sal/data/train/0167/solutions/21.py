class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        mem = [[None for _ in range(N)] for _ in range(K - 1)]

        def dp(k, n, mem):
            if n <= 1 or k == 1:
                return n
            if mem[k - 2][n - 1] is None:
                l, r = 1, n
                while l + 1 < r:
                    i = (l + r) // 2
                    if dp(k - 1, i - 1, mem) < dp(k, n - i, mem):
                        l = i
                    elif dp(k - 1, i - 1, mem) > dp(k, n - i, mem):
                        r = i
                    else:
                        l = r = i
                mem[k - 2][n - 1] = min(max(dp(k - 1, l - 1, mem), dp(k, n - l, mem)), max(dp(k - 1, r - 1, mem), dp(k, n - r, mem))) + 1
            return mem[k - 2][n - 1]
        return dp(K, N, mem)

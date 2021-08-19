class Solution:

    def soupServings(self, N: int) -> float:
        compressed_N = N // 25
        N = compressed_N + (1 if N - compressed_N * 25 > 0 else 0)
        mem = {}

        def dp(a, b):
            if (a, b) in mem:
                return mem[a, b]
            else:
                if a <= 0 or b <= 0:
                    result = 0.5 if a <= 0 and b <= 0 else 1.0 if a <= 0 else 0.0
                else:
                    result = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
                mem[a, b] = result
                return result
        if N <= 100:
            return dp(N, N)
        else:
            for i in range(100, N + 1):
                current_result = dp(i, i)
                if 1 - current_result < 1e-06:
                    return 1.0
            return current_result

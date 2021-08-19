class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        # Mathematical
        # Sum_{j > i} (2^(j - i - 1)) x (A_j - A_i) = Sum_{i = 0}^{n - 1} (2^i - 2^(N - i - 1)) x A_i
        # Time  complexity: O(NlogN), where N is the length of A.
        # Space complexity: O(N)
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N - i - 1]) * x) % MOD

        return ans

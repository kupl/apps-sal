class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7

        N = n
        R = len(rollMax)

        # Set up DP.
        T = [0] * (N + 1)
        D = [[0] * R for _ in range(N + 1)]

        # Base cases.
        T[0] = 1
        T[1] = R
        D[1] = [1] * R

        # Compute.
        for i in range(2, N + 1):  # Roll number.
            for j in range(R):  # Face number.
                lim = max(i - rollMax[j], 0)
                for k in range(i - 1, lim - 1, -1):  # num rolls given last `k` in sequence are `j`
                    D[i][j] += T[k] - D[k][j]
            T[i] = sum(D[i])

        return sum(D[-1]) % mod

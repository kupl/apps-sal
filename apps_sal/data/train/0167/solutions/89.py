class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        DP = range(N + 1)
        for k in range(2, K + 1):
            DP2 = [0]
            x = 1
            for n in range(1, N + 1):
                while x < n and max(DP[x - 1], DP2[n - x]) > max(DP[x], DP2[n - x - 1]):
                    x += 1

                DP2.append(1 + max(DP[x - 1], DP2[n - x]))

            DP = DP2

        return DP[-1]

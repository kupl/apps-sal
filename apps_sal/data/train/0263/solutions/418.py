class Solution:

    def knightDialer(self, N: int) -> int:
        if N == 0:
            return 0
        d = {}
        choices = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

        def dp(k, n):
            if n == 0:
                return 1
            if n == 1:
                return len(choices[k])
            if (k, n) not in d:
                d[k, n] = sum([dp(nxt, n - 1) for nxt in choices[k]])
            return d[k, n]
        return sum([dp(v, N - 1) for v in range(10)]) % (10 ** 9 + 7)

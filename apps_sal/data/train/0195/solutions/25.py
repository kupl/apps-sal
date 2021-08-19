class Solution:

    def countTriplets(self, A: List[int]) -> int:
        two_and_count = collections.Counter()
        res = 0
        for (idx, x) in enumerate(A):
            if x == 0:
                res += 1
            new_two_and = collections.Counter([x])
            for idy in range(idx):
                if x & A[idy] == 0:
                    res += 3
                new_two_and[A[idy] & x] += 2
            for (v, c) in two_and_count.items():
                if x & v == 0:
                    res += 3 * c
            two_and_count += new_two_and
        return res

    def countTriplets_II(self, A: List[int]) -> int:
        M = 3
        N = 1 << 16
        dp = [[0] * N for _ in range(M + 1)]
        dp[0][N - 1] = 1
        for m in range(1, M + 1):
            for v in range(N):
                for a in A:
                    dp[m][v & a] += dp[m - 1][v]
        return dp[M][0]

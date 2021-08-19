class Solution:

    def knightDialer(self, N: int) -> int:
        cac = {}
        MOD = 10 ** 9 + 7
        pmvs = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [4, 2]]

        def d(k, i):
            try:
                return cac[k, i]
            except:
                pass
            if k == 0:
                return 1
            s = 0
            for j in pmvs[i]:
                s += d(k - 1, j) % MOD
            cac[k, i] = s % MOD
            return cac[k, i]
        ans = 0
        for i in range(10):
            ans += d(N - 1, i) % MOD
        return ans % MOD

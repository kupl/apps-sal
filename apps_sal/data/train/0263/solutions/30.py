class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7

        d = dict()
        d[0] = {4, 6}
        d[1] = {6, 8}
        d[2] = {7, 9}
        d[3] = {4, 8}
        d[4] = {0, 3, 9}
        d[6] = {0, 1, 7}
        d[7] = {2, 6}
        d[8] = {1, 3}
        d[9] = {2, 4}

        memo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        memo2 = [0] * 10

        for i in range(2, n + 1):
            for key, val in list(d.items()):
                for v in val:
                    memo2[key] += memo[v]
            memo = memo2
            memo2 = [0] * 10

        return sum(memo) % mod

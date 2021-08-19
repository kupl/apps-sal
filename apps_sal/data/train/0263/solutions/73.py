"""
 0. 1. 2. 3. 4. 5. 6. 7. 8. 9
[2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
[6, 5, 0, 0, 0, 0, 0, 0, 0, 0]

[6, 5, 4, 5, 6, 0, 6, 5, 4, 5]


"""


class Solution(object):

    def knightDialer(self, N):
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for hops in range(N - 1):
            dp2 = [0] * 10
            for (node, count) in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
            dp = dp2
        print(dp)
        return sum(dp) % MOD

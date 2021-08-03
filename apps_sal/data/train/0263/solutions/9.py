class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        memo = [1] * 10
        maxV = (10**9 + 7)
        for _ in range(N - 1):
            temp = [0] * 10
            for i in range(10):
                for dest in moves[i]:
                    temp[i] += memo[dest]
                temp[i] %= (10**9 + 7)
            memo = temp

        return sum(memo) % (10**9 + 7)

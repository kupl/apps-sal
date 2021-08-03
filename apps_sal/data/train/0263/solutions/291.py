class Solution:
    def knightDialer(self, n: int) -> int:
        self.knight_movable_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        self.dp = [[None for _ in range(10)] for _ in range(n)]

        def traverse(dial, remaining):
            if remaining == 0:
                return 1
            if self.dp[remaining][dial] is not None:

                return self.dp[remaining][dial]

            cnt = 0
            for next_dial in self.knight_movable_map[dial]:
                cnt += traverse(next_dial, remaining - 1)

            self.dp[remaining][dial] = cnt
            return cnt

        cnt = 0
        for i in range(10):
            cnt += traverse(i, n - 1)

        modulo_num = 10**9 + 7

        return cnt % modulo_num

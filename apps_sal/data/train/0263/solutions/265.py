class Solution:
    def knightDialer(self, n: int) -> int:
        map = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        memo = [[-1] * n for i in range(len(map))]

        def recur(num, hops, memo):
            if hops < 0:
                return 0
            elif hops == 0:
                return 1

            if memo[num][hops] == -1:
                s = 0
                for move in map[num]:
                    s += recur(move, hops - 1, memo)

                memo[num][hops] = s
            return memo[num][hops]

        s = 0
        for key in range(len(map)):
            s += recur(key, n - 1, memo)

        return s % (10 ** 9 + 7)

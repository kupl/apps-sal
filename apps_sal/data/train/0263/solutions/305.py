class Solution:

    def recur_helper(self, num, n, cnt, memo, next_moves):

        if n == 0:
            return cnt

        key = (num, n)
        if key in memo:
            return memo[key]

        cnt = 0
        for next_num in next_moves[num]:
            cnt += self.recur_helper(next_num, n - 1, 1, memo, next_moves)

        memo[key] = cnt

        return memo[key]

    def knightDialer(self, n: int) -> int:
        next_moves = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [9, 3, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        memo = dict()
        cnt = 0
        for num in range(10):
            cnt += self.recur_helper(num, n - 1, 1, memo, next_moves)

        return cnt % (10 ** 9 + 7)

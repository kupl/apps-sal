class Solution:
    def knightDialer(self, n: int) -> int:
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        dirc = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        mod = 10**9 + 7
        mem = {}

        def dfs(i, j, k):
            if k == 1:
                return 1
            if (i, j, k) in mem:
                return mem[(i, j, k)]
            ans = 0
            for x, y in dirc:
                if -1 < i + x < 4 and -1 < j + y < 3 and board[i + x][j + y] != '#' and board[i + x][j + y] != '*':
                    ans += dfs(i + x, j + y, k - 1) % mod
            ans %= mod
            mem[(i, j, k)] = ans
            return ans
        res = 0
        for i in range(3):
            for j in range(3):
                res += dfs(i, j, n) % mod
        res = (res + dfs(3, 1, n)) % mod
        return res

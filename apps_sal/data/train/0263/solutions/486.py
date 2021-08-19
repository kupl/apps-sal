class Solution:
    DIAL = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    def knightDialer(self, n: int) -> int:
        directions = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        count = 0
        m = len(self.DIAL)
        nn = len(self.DIAL[0])
        cache = {}

        def jump(i, j, path_length):
            if path_length == n:
                return 1
            else:
                total = 0
                if (i, j, path_length) in cache:
                    return cache[i, j, path_length]
                for (inc_r, inc_c) in directions:
                    r = i + inc_r
                    c = j + inc_c
                    if 0 <= r < m and 0 <= c < nn and isinstance(self.DIAL[r][c], int):
                        total += jump(r, c, path_length + 1)
                cache[i, j, path_length] = total
                return total
        res = 0
        for i in range(m):
            for j in range(nn):
                if isinstance(self.DIAL[i][j], int):
                    res += jump(i, j, 1)
        return res % (10 ** 9 + 7)

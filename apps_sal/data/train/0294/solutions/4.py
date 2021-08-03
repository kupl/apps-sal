class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        diag_lr = [True] * (2 * n - 1)
        diag_rl = [True] * (2 * n - 1)
        vert = [True] * n
        res = []

        def _check_board(x, y):
            return vert[y] and diag_lr[y - x + n - 1] and diag_rl[x + y]

        def _helper(x):
            if x == n:
                res.append(1)
                return
            for y in range(n):
                if _check_board(x, y):
                    vert[y] = False
                    diag_lr[y - x + n - 1] = False
                    diag_rl[x + y] = False
                    _helper(x + 1)
                    vert[y] = True
                    diag_lr[y - x + n - 1] = True
                    diag_rl[x + y] = True

        _helper(0)
        return len(res)

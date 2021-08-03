class Solution:

    def find_arrangements(self, arrangement, diag1_used, diag2_used, col_used, x, n):
        if x == n:
            return 1
        res = 0
        for y in range(n):
            diag1 = x + y
            diag2 = x - y + n
            if not diag1_used[diag1] and not diag2_used[diag2] and not col_used[y]:
                arrangement.append(y)
                diag1_used[diag1] = True
                diag2_used[diag2] = True
                col_used[y] = True
                cur_res = self.find_arrangements(arrangement, diag1_used, diag2_used, col_used, x + 1, n)
                arrangement.pop()
                diag1_used[diag1] = False
                diag2_used[diag2] = False
                col_used[y] = False
                res += cur_res

        return res

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        arrangement = []
        diag1_used = [False] * (2 * n)
        diag2_used = [False] * (2 * n)
        col_used = [False] * n
        return self.find_arrangements(arrangement, diag1_used, diag2_used, col_used, 0, n)

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        def solve(rows, cols, diag0, diag1, n):
            nonlocal count

            freerows = {i for i in range(n)} - rows
            if not freerows:
                count += 1
                return

            i = freerows.pop()
            candidates = []
            for j in range(n):
                if j in cols:
                    continue
                if i + j in diag0:
                    continue
                if i - j in diag1:
                    continue

                rows.add(i)
                cols.add(j)
                diag0.add(i + j)
                diag1.add(i - j)

                solve(rows, cols, diag0, diag1, n)

                rows.remove(i)
                cols.remove(j)
                diag0.remove(i + j)
                diag1.remove(i - j)

        solve(set(), set(), set(), set(), n)
        return count

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        placement = []

        def can_place_queen(row, col):
            for i, j in enumerate(placement):
                if col == j or abs(col - j) == row - i:
                    return False
            return True

        def place_in_row(row):
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if can_place_queen(row, col):
                    placement.append(col)
                    count += place_in_row(row + 1)
                    placement.pop()
            return count
        return place_in_row(0)

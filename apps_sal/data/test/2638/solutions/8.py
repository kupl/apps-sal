class Solution:

    def minimumTotal(self, triangle):
        row = [triangle[0][0]]
        for i in range(1, len(triangle)):
            new_row = []
            for j in range(len(row) + 1):
                new_row.append(triangle[i][j] + min(row[j - 1] if j - 1 >= 0 else sys.maxsize, row[j] if j < len(row) else sys.maxsize))
            row = new_row
        return min(row)

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
         For each position (column) C within a row R,
         the minimum path sum that leads to (r, c) is defined as:
         min_path_sum[r][c] = min(min_path_sum[r-1][adj] for adj in adjacent columns of (r,c)) + triangle[r][c]
         """

        if not triangle or not triangle[0]:
            return 0

        min_path_sum = [[0] * len(triangle) for row in range(len(triangle))]
        min_path_sum[0][0] = triangle[0][0]

        ROWS = len(triangle)

        def get_valid_adjacents_of(row, col):
            if col == 0:
                return [(row - 1, col)]
            if col == row:
                return [(row - 1, col - 1)]
            return [(row - 1, col - 1), (row - 1, col)]

        for row in range(1, ROWS):
            for col in range(0, row + 1):
                adjacents = get_valid_adjacents_of(row, col)
                min_path_sum[row][col] = triangle[row][col] + min(min_path_sum[r][c] for r, c in adjacents)

        return min(min_path_sum[-1])

class Solution:

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        '\n         Time O(r*c) because we iterate through the wall once and do O(1) work for each element\n         in the wall.\n         Space O(c) because in the worst case, our hashmap will have length c.\n         '
        if not wall:
            return 0
        '\n         The maximum number of bricks we have to intersect is the equal to the number of rows,\n         in the case that we have to intersect a brick at every row.\n         columns will be a map from a column to the number of bricks that would be intersected\n         if we drew a line through that column. For now, we assume that every column will intersect\n         the maximum number of bricks, which is the number of rows in the wall.\n         '
        numRows = len(wall)
        columns = collections.defaultdict(lambda: numRows)
        for r in range(len(wall)):
            '\n            col will be the current column that we are considering drawing a line through.\n            If a brick in this row ends at column col, then we can avoid intersecting that\n            brick by drawing a line through column col.\n            '
            col = 0
            for c in range(len(wall[r]) - 1):
                '\n                Add the length of the current brick to col to find the column where\n                this brick ends.\n                '
                col += wall[r][c]
                "\n                 Because this brick ends at col, it won't be intersected if we draw a line\n                 at column col. So we can decrement the number of bricks that will be intersected \n                 if we draw a line at column col.\n                 "
                columns[col] -= 1
        return numRows if len(columns) == 0 else min(columns.values())

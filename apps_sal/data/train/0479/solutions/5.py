class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        """
         Time O(r*c) because we iterate through the wall once and do O(1) work for each element
         in the wall.
         Space O(c) because in the worst case, our hashmap will have length c.
         """
        if not wall:
            return 0

        """
         The maximum number of bricks we have to intersect is the equal to the number of rows,
         in the case that we have to intersect a brick at every row.
         columns will be a map from a column to the number of bricks that would be intersected
         if we drew a line through that column. For now, we assume that every column will intersect
         the maximum number of bricks, which is the number of rows in the wall.
         """
        numRows = len(wall)
        columns = collections.defaultdict(lambda: numRows)

        for r in range(len(wall)):
            """
            col will be the current column that we are considering drawing a line through.
            If a brick in this row ends at column col, then we can avoid intersecting that
            brick by drawing a line through column col.
            """
            col = 0
            for c in range(len(wall[r]) - 1):
                """
                Add the length of the current brick to col to find the column where
                this brick ends.
                """
                col += wall[r][c]
                """
                 Because this brick ends at col, it won't be intersected if we draw a line
                 at column col. So we can decrement the number of bricks that will be intersected 
                 if we draw a line at column col.
                 """
                columns[col] -= 1

        return numRows if len(columns) == 0 else min(columns.values())

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall:
            return 0

        width = sum(wall[0])
        length = len(wall)
        columns = collections.defaultdict(lambda: length)

        for r in range(len(wall)):
            col = 0
            for c in range(len(wall[r]) - 1):
                col += wall[r][c]
                columns[col] -= 1

        return length if len(columns) == 0 else min(columns.values())

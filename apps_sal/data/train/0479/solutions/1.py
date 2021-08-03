class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        x_to_edge_dict = {}
        rows = len(wall)
        cols = 0
        if rows > 0:
            cols = len(wall[0])

        for row in range(rows):
            last_pos = 0
            for brick in wall[row][:-1]:  # -1 to ignore end of last brick
                end = last_pos + brick
                if end not in x_to_edge_dict:
                    x_to_edge_dict[end] = 1
                else:
                    x_to_edge_dict[end] += 1
                last_pos = end

        # print(x_to_edge_dict)
        if x_to_edge_dict == {}:
            return rows
        else:
            return rows - max(x_to_edge_dict.values())

class Solution:
    """
    def minimumTotal(self, triangle):
        cost = [[0 for j in range(len(i))] for i in triangle]
        for row in range(len(triangle)):
            for col in range(len(triangle[row])):
                if row == 0:
                    cost[row][col] = triangle[row][col]
                else:
                    if col-1 >= 0 and col < len(triangle[row-1]):
                        cost[row][col] = min(cost[row-1][col-1]+triangle[row][col],cost[row-1][col]+triangle[row][col])
                    elif col-1 >= 0:
                        cost[row][col] = cost[row-1][col-1]+triangle[row][col]
                    elif col < len(triangle[row-1]):
                        cost[row][col] = cost[row-1][col]+triangle[row][col]
        return min(cost[len(triangle)-1])
    """

    def minimumTotal(self, triangle):
        cost = [[0 for j in range(len(triangle))] for i in range(2)]
        for row in range(len(triangle)):
            for col in range(len(triangle[row])):
                if row == 0:
                    cost[row][col] = triangle[row][col]
                elif col - 1 >= 0 and col < len(triangle[row - 1]):
                    cost[row % 2][col] = min(cost[(row - 1) % 2][col - 1] + triangle[row][col], cost[(row - 1) % 2][col] + triangle[row][col])
                elif col - 1 >= 0:
                    cost[row % 2][col] = cost[(row - 1) % 2][col - 1] + triangle[row][col]
                elif col < len(triangle[row - 1]):
                    cost[row % 2][col] = cost[(row - 1) % 2][col] + triangle[row][col]
        return min(cost[(len(triangle) - 1) % 2])

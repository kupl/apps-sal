class Solution:
    def get_index_ones(self, row_list, current_columns, columns_to_check):
        counter = 0
        for i in current_columns:
            if row_list[i] == 1:
                if columns_to_check.get(i) == None:
                    columns_to_check[i] = 1
                else:
                    columns_to_check[i] = columns_to_check[i] + 1
                # current_columns.remove(i)

    def countServers(self, grid: List[List[int]]) -> int:
        row_dim = len(grid)
        column_dim = len(grid[0])
        result = 0
        map_single = []
        current_columns = [i for i in range(column_dim)]
        columns_to_check = {}
        for x in range(row_dim):
            if 1 in grid[x]:
                difference = column_dim - len([i for i in grid[x] if i == 0])
                # more than 1
                if difference > 1:
                    self.get_index_ones(grid[x], current_columns, columns_to_check)
                    result += difference
                else:
                    self.get_index_ones(grid[x], current_columns, columns_to_check)
                    map_single.append(grid[x])
        for row in map_single:
            for y, repeat in columns_to_check.items():
                if row[y] == 1 and repeat > 1:
                    result += 1
        return result

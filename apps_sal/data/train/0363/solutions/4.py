class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        area_of_enclaves = 0

        def traverse(x, y):
            area = 1
            A[x][y] = 0
            enclave = True
            for x_direction, y_direction in directions:
                new_x = x + x_direction
                new_y = y + y_direction
                if 0 <= new_x < len(A) and 0 <= new_y < len(A[0]):
                    if A[new_x][new_y] == 1:
                        area_of_traverse, enclave_traverse = traverse(new_x, new_y)
                        area += area_of_traverse
                        if not enclave_traverse:
                            enclave = False
                else:
                    enclave = False
            return area, enclave

        for x, row in enumerate(A):
            for y, data in enumerate(row):
                if data == 1:
                    area, enclave = traverse(x, y)
                    if enclave:
                        area_of_enclaves += area
        return area_of_enclaves

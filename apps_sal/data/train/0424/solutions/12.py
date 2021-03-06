class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        def get_movement(a, b):
            x = a[0] - b[0]
            y = a[1] - b[1]
            return (x, y)

        def check_movement(move):
            counter = 0
            for val in B_elements:
                x = val[0] + move[0]
                y = val[1] + move[1]
                if (x, y) in A_elements:
                    counter += 1
            return counter
        A_elements = set()
        B_elements = []
        dimension = None
        for (i, row) in enumerate(A):
            for (j, val) in enumerate(row):
                if val == 1:
                    A_elements.add((i, j))
                if B[i][j] == 1:
                    B_elements.append((i, j))
        dimension = i + 1
        maximo = 0
        A_len = len(A_elements)
        B_len = len(B_elements)
        maximo_posible = min(A_len, B_len)
        moved = {}
        for elem_A in A_elements:
            for elem_B in B_elements:
                move = get_movement(elem_A, elem_B)
                if move not in list(moved.keys()):
                    moved[move] = 1
                else:
                    moved[move] += 1
                if moved[move] > maximo:
                    maximo = moved[move]
                    if maximo >= maximo_posible:
                        break
        print(moved)
        return maximo

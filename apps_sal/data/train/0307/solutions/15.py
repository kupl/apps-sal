class Solution:
    def soupServings(self, N: int) -> float:
        import numpy as np
        if N > 5000:
            return 1
        if N == 0:
            return 0.5
        if N % 25 == 0:
            N = N // 25
        else:
            N = N // 25 + 1

        Matrix = [[0.0 for i in range(N + 1)] for j in range(N + 1)]

        Matrix = np.matrix(Matrix)
        Matrix[N, N] = 1

        Explore_List = [(N, N)]
        while(Explore_List):
            New_List = set()
            for x, y in Explore_List:
                if(x != 0 and y != 0):
                    Matrix[max(0, x - 2), max(0, y - 2)] += Matrix[x, y] * 1 / 4
                    New_List.add((max(0, x - 2), max(0, y - 2)))
                    Matrix[max(0, x - 1), max(0, y - 3)] += Matrix[x, y] * 1 / 4
                    New_List.add((max(0, x - 1), max(0, y - 3)))
                    Matrix[max(0, x - 3), max(0, y - 1)] += Matrix[x, y] * 1 / 4
                    New_List.add((max(0, x - 3), max(0, y - 1)))
                    Matrix[max(0, x - 4), max(0, y - 0)] += Matrix[x, y] * 1 / 4
                    New_List.add((max(0, x - 4), max(0, y - 0)))

            Explore_List = New_List

        return Matrix[0].sum() - 1 / 2 * Matrix[0, 0]

class Solution:
    def knightDialer(self, N: int) -> int:
        T = [[0] * (N+1) for i in range(10)]
        for i in range(10):
            T[i][1] = 1
        for step in range(2, N+1):
            T[0][step] = T[4][step-1] + T[6][step-1]
            T[1][step] = T[8][step-1] + T[6][step-1]
            T[2][step] = T[7][step-1] + T[9][step-1]
            T[3][step] = T[4][step-1] + T[8][step-1]
            T[4][step] = T[3][step-1] + T[9][step-1] + T[0][step-1]
            T[5][step] = 0
            T[6][step] = T[1][step-1] + T[7][step-1] + T[0][step-1]
            T[7][step] = T[6][step-1] + T[2][step-1]
            T[8][step] = T[1][step-1] + T[3][step-1]
            T[9][step] = T[2][step-1] + T[4][step-1]
        return sum([T[i][N] for i in range(10)]) % (pow(10, 9) + 7)


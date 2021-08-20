class Solution:

    def knightDialer(self, N: int) -> int:
        D = [[0] * 10 for _ in range(N)]
        D[0] = [1] * 10
        for i in range(1, N):
            P = D[i - 1]
            D[i][1] = P[8] + P[6]
            D[i][2] = P[7] + P[9]
            D[i][3] = P[4] + P[8]
            D[i][4] = P[3] + P[9] + P[0]
            D[i][5] = 0
            D[i][6] = P[1] + P[7] + P[0]
            D[i][7] = P[2] + P[6]
            D[i][8] = P[1] + P[3]
            D[i][9] = P[2] + P[4]
            D[i][0] = P[4] + P[6]
        return sum(D[-1]) % (10 ** 9 + 7)

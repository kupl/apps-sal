class Solution:
    def knightDialer(self, N: int) -> int:
        D = [[0] * 10 for _ in range(2)]
        D[0] = [1] * 10
        for i in range(1, N):
            idx = i % 2
            P = D[(i - 1) % 2]
            D[idx][1] = P[8] + P[6]
            D[idx][2] = P[7] + P[9]
            D[idx][3] = P[4] + P[8]
            D[idx][4] = P[3] + P[9] + P[0]
            D[idx][5] = 0
            D[idx][6] = P[1] + P[7] + P[0]
            D[idx][7] = P[2] + P[6]
            D[idx][8] = P[1] + P[3]
            D[idx][9] = P[2] + P[4]
            D[idx][0] = P[4] + P[6]

        return sum(D[(N + 1) % 2]) % (10**9 + 7)

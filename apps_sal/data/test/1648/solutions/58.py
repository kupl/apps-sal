import sys
sys.setrecursionlimit(1 << 30)
M = 10**9 + 7
N, Blue = map(int, input().split())
Red = N - Blue
Comb = [[0] * (N + 1) for i in range(0, N + 1)]
for i in range(1, N + 1):
    Comb[i][0] = 1
    Comb[i][1] = i
    Comb[i][i] = 1
Comb[0][0] = 1
for i in range(1, N + 1):
    for j in range(2, i + 1):
        Comb[i][j] = (Comb[i - 1][j] + Comb[i - 1][j - 1]) % M
for i in range(1, Blue + 1):
    A = Comb[Red + 1][i] * Comb[Blue - 1][i - 1]
    print(A % M)

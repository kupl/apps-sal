(n, t) = list(map(int, input().split()))
't = 10000\nfor n in range(10,11):\n    T = [[-1 for _ in range(i)] for i in range(1,n+1)]\n    G = [[0 for _ in range(i)] for i in range(1,n+2)]\n    for i in range(t):\n        G[0][0] += 1000000000000\n        for j in range(n):\n            for l in range(j+1):\n                if G[j][l] >= 1000000000000:\n                    G[j+1][l] += (G[j][l]-1000000000000)//2\n                    G[j+1][l+1] += (G[j][l]-1000000000000)//2\n                    G[j][l] = 1000000000000\n                    if T[j][l] == -1:\n                        T[j][l] = i\n    print(T)\nint(input())'
R = [[0], [2, 2], [6, 4, 6], [14, 8, 8, 14], [30, 13, 10, 13, 30], [62, 21, 15, 15, 21, 62], [126, 36, 21, 18, 21, 36, 126], [254, 62, 30, 23, 23, 30, 62, 254], [510, 104, 45, 31, 27, 31, 45, 104, 510], [1022, 181, 68, 40, 33, 33, 40, 68, 181, 1022]]
C = [0 for _ in range(10001)]
for i in range(n):
    for j in range(i + 1):
        C[R[i][j]] += 1
for i in range(1, 10001):
    C[i] += C[i - 1]
if t:
    print(C[t - 1])
else:
    print(0)

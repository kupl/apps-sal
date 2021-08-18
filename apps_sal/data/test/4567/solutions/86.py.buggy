N, *S = list(map(int, open(0).read().split()))

p = [[False for i in range(100 * 100 + 1)] for j in range(N + 1)]

p[0][0] = True

for i in range(N):
    for j in range(100 * N + 1):
        # S0~Si, point sum is j
        if p[i][j] == True:
            # incorrect
            p[i + 1][j] = True
            # correct
            p[i + 1][j + S[i]] = True

for i in range(100 * N, -1, -1):
    if p[N][i] == True and i % 10 != 0:
        print(i)
        return

print((0))

N, M = list(map(int, input().split()))
X = [[int(a) for a in input().split()] for i in range(N)]
i0, j0 = -1, -1
for i in range(N):
    for j in range(M - 1):
        if X[i][j] != X[i][j + 1]:
            i0, j0 = i, j + 1
            break
    if i0 >= 0:
        break

s = 0
for i in range(N):
    s ^= X[i][0]
if s > 0:
    print("TAK")
    print(*([1] * N))
elif i0 >= 0:
    print("TAK")
    print(*([1] * i0 + [j0 + 1] + [1] * (N - i0 - 1)))
else:
    print("NIE")

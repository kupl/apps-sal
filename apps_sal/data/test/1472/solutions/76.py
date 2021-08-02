N, X, Y = map(int, input().split())
ansvec = [0] * N
for a in range(N - 1):
    for b in range(a + 1, N):
        ansvec[min(b - a, abs(a - X + 1) + abs(b - Y + 1) + 1)] += 1
for k in range(N - 1):
    print(ansvec[k + 1])

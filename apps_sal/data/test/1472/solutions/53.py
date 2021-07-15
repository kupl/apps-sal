N, X, Y = [int(x) for x in input().split()]

D = [0 for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1, N + 1):
        D[min(j - i, abs(i - X) + 1 + abs(j - Y))] += 1

for i in range(1, N):
    print((D[i]))


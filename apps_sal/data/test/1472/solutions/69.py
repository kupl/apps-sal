(N, X, Y) = [int(x) for x in input().split()]
counter = [0] * N
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        d = min(abs(i - j), abs(i - X) + abs(j - Y) + 1, abs(i - Y) + abs(j - X) + 1)
        counter[d] += 1
for i in range(1, N):
    print(counter[i])

N, X, Y = list(map(int, input().split()))


def f(i, j):
    v1 = j - i
    v2 = abs(X - i) + 1 + abs(j - Y)
    v3 = abs(Y - i) + 1 + abs(j - X)
    return min(v1, v2, v3)


D = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        d = f(i, j)
        D[d] += 1

for d in D[1:]:
    print(d)


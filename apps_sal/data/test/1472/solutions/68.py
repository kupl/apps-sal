(N, X, Y) = map(int, input().split())
X -= 1
Y -= 1


def min_dist(i, j):
    d1 = abs(i - j)
    d2 = abs(X - i) + abs(Y - j) + 1
    return min(d1, d2)


ans = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        ans[min_dist(i, j)] += 1
[print(a) for a in ans[1:]]

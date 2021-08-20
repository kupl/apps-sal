N = int(input())
(R, d, f, s) = (sorted((list(map(int, input().split())) for i in range(N))) + [(2000000000.0, 0)], [0] * N + [1], [0] * N, 1)
for i in range(N - 1, -1, -1):
    x = i + 1
    while x < N and R[x][0] < sum(R[i]):
        x = f[x]
    f[i] = x
    d[i] = s = (s + d[x]) % 998244353
print(d[0])

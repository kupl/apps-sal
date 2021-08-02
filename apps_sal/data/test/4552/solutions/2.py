N = int(input())

F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')
for i in range(1, 1 << 10):
    g = [0] * N
    for j in range(10):
        if i >> j & 1:
            for k in range(N):
                g[k] += F[k][j]
    sub = 0
    for i in range(N):
        sub += P[i][g[i]]
    ans = max(ans, sub)
print(ans)

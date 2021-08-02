N, M = list(map(int, input().split()))
d = [[1000000] * N for _ in range(N)]
d_dict = {}

inf = 0
for i in range(M):
    a, b, c = list(map(int, input().split()))
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
    d_dict[(a - 1, b - 1)] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for key in d_dict:
    if d[key[0]][key[1]] < d_dict[key]:
        ans += 1

print(ans)

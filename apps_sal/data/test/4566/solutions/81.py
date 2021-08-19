(N, M) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
ans = [0 for _ in range(N)]
n = 1
while True:
    for i in range(M):
        for j in range(2):
            if n == ab[i][j]:
                ans[n - 1] += 1
    if n == N:
        break
    n += 1
for i in range(N):
    print(ans[i])

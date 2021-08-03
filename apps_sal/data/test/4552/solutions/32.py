N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -1000000000
for i in range(1, 1 << 10):
    cnt = [0 for _ in range(N)]
    for j in range(10):
        if (i >> j) % 2 == 1:
            for k in range(N):
                cnt[k] += F[k][j]
    A = [P[j][cnt[j]] for j in range(N)]
    ans = max(ans, sum(A))
print(ans)

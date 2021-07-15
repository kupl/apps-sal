N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -9999999999
for i in range(1, 2 ** 10):
    s = 0
    for j in range(N):
        cnt = 0
        for k in range(10):
            if i >> k & 1 and F[j][k] == 1:
                cnt += 1
        s += P[j][cnt]
    ans = max(ans, s)
print(ans)

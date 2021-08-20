import itertools
N = int(input())
F = []
for _ in range(N):
    F.append(list(map(int, input().split())))
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))
ans = sum([min(a) for a in P])
for b in range(1, 1024):
    b = list(map(int, format(b, '010b')))
    tmp = 0
    for i in range(N):
        cnt = 0
        for (j, x) in enumerate(b):
            cnt += F[i][j] * x
        tmp += P[i][cnt]
    ans = max(ans, tmp)
print(ans)

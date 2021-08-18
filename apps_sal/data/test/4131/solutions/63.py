N, M = list(map(int, input().split()))
D = [[]for _ in range(N)]

for i in range(M):
    p, y = list(map(int, input().split()))
    D[p - 1].append((y, i))
ans = [0] * M

for i, d in enumerate(D):
    d.sort()
    for k, (y, j) in enumerate(d):
        ans[j] = str(i + 1).zfill(6) + str(k + 1).zfill(6)

print(('\n'.join(ans)))

N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

path = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    path[a].append(b)
    path[b].append(a)

ans = 0
for i, p in enumerate(path):
    h = H[i]
    tmp = 0
    for pp in p:
        tmp = max(tmp, H[pp])
    if tmp < h:
        ans += 1

print(ans)

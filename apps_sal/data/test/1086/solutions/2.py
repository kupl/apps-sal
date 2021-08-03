h, w = map(int, input().split())

bitdp = [[0 for j in range(w)] for i in range(h)]
al = []
bl = []
for _ in range(h):
    a = list(map(int, input().split()))
    al.append(a)
for _ in range(h):
    b = list(map(int, input().split()))
    bl.append(b)
abl = [[] for i in range(h)]
for i in range(h):
    for j in range(w):
        abl[i].append(abs(al[i][j] - bl[i][j]))

bitdp[0][0] = 1 << h * w + abl[0][0]
for i in range(h):
    for j in range(w):
        if j != w - 1:
            bitdp[i][j + 1] |= bitdp[i][j] << abl[i][j + 1] | bitdp[i][j] >> abl[i][j + 1]
        if i != h - 1:
            bitdp[i + 1][j] |= bitdp[i][j] << abl[i + 1][j] | bitdp[i][j] >> abl[i + 1][j]

ans = []
for i in range(h * w * 2 + 1):
    if (bitdp[-1][-1] >> i & 1):
        ans.append(abs(h * w - i))

print(min(ans))

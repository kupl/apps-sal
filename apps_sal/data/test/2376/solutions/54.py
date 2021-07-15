def makelst(lst, v):
    for i in range(N):
        if wv[i][0] == v:
            lst.append(wv[i][1])
    lst.sort(reverse=True)

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
v1cnt = W // wv[0][0]
v2cnt = W // (wv[0][0] + 1)
v3cnt = W // (wv[0][0] + 2)
v4cnt = W // (wv[0][0] + 3)
v1, v2, v3, v4 = [], [], [], []
makelst(v1, wv[0][0])
makelst(v2, wv[0][0] + 1)
makelst(v3, wv[0][0] + 2)
makelst(v4, wv[0][0] + 3)

[0] + v1, [0] + v2, [0] + v3, [0] + v4

ans = 0

v1cnt = min(v1cnt, len(v1))
v2cnt = min(v2cnt, len(v2))
v3cnt = min(v3cnt, len(v3))
v4cnt = min(v4cnt, len(v4))
ru1 = [0] * (v1cnt + 1)
ru2 = [0] * (v2cnt + 1)
ru3 = [0] * (v3cnt + 1)
ru4 = [0] * (v4cnt + 1)
for i in range(1, v1cnt + 1):
    ru1[i] = ru1[i - 1] + v1[i - 1]

for i in range(1, v2cnt + 1):
    ru2[i] = ru2[i - 1] + v2[i - 1]

for i in range(1, v3cnt + 1):
    ru3[i] = ru3[i - 1] + v3[i - 1]

for i in range(1, v4cnt + 1):
    ru4[i] = ru4[i - 1] + v4[i - 1]

for i in range(len(ru1)):
    for j in range(len(ru2)):
        for k in range(len(ru3)):
            for l in range(len(ru4)):
                wtmp = (i * wv[0][0]) + (j * (wv[0][0] + 1)) + (k * (wv[0][0] + 2)) + (l * (wv[0][0] + 3))
                if wtmp <= W:
                    ans = max(ans, ru1[i] + ru2[j] + ru3[k] + ru4[l])

print(ans)

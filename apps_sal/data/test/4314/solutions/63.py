(h, w) = map(int, input().split())
a = [input() for i in range(h)]
vdel = []
sdel = []
for i in range(h):
    if a[i].count('.') == w:
        sdel.append(i)
for i in range(w):
    cnt = 0
    for j in range(h):
        if a[j][i] == '.':
            cnt += 1
    if cnt == h:
        vdel.append(i)
i = 0
lens = len(sdel) - 1
h -= lens + 1
while i <= lens:
    del a[sdel[lens]]
    lens -= 1
for i in range(h):
    tmp = ''
    for j in range(w):
        if j not in vdel:
            tmp += a[i][j]
    print(tmp)

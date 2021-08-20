n = int(input())
s = input()
(r, g, b) = ([], [], [])
cnt = 1
for i in s:
    if i == 'R':
        r.append(cnt)
    elif i == 'G':
        g.append(cnt)
    else:
        b.append(cnt)
    cnt += 1
rd = set(map(lambda x: x * 2, r))
gd = set(map(lambda x: x * 2, g))
bd = set(map(lambda x: x * 2, b))
ddc = 0
for i in r:
    for j in g:
        if i + j in bd:
            ddc += 1
for j in g:
    for k in b:
        if j + k in rd:
            ddc += 1
for i in r:
    for k in b:
        if i + k in gd:
            ddc += 1
print(len(r) * len(g) * len(b) - ddc)

a = input('').split(' ')
n = int(a[0])
m = int(a[1])
x = list(map(int, input('').split(' ')))
d = {}
for xx in x:
    d[xx] = True

i = 0
c = 0
pos = [[]]
pos.append([])
cur = 0
pos[cur] = x.copy()
ys = []
ans = 0
while(i < m):
    c += 1
    pos[cur ^ 1] = []
    for k in pos[cur]:
        if(k + 1 not in d):
            pos[cur ^ 1].append(k + 1)
            d[k + 1] = True
        if(k - 1 not in d):
            pos[cur ^ 1].append(k - 1)
            d[k - 1] = True
    res = False
    cur = cur ^ 1
    for p in pos[cur]:
        i += 1
        ys.append(p)
        ans += c
        if(i == m):
            res = True
            break
    if(res):
        break

print(ans)
for h in ys:
    print(h, end=' ')

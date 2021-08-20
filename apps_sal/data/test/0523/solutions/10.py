(n, m) = list(map(int, input().split()))
s = [input() for i in range(n)]
d = {}
for i in s:
    try:
        d[i] += 1
    except:
        d[i] = 1
revis = []
pal = ''
for i in d:
    revi = i[::-1]
    if revi == i:
        if d[i] & 1:
            if len(i) > len(pal):
                pal = i
        else:
            x = d[i] // 2
            for j in range(x):
                revis.append(i)
    elif revi in d:
        x = min(d[i], d[revi])
        d[i] -= x
        d[revi] -= x
        for j in range(x):
            revis.append(i)
ss = ''
for i in revis:
    ss += i
ss = ss + pal + ss[::-1]
print(len(ss))
print(ss)

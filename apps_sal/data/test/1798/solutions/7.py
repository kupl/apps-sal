n = int(input())
a = list(map(int, input().split()))
u = {}
v = {}
w = []
for (i, x) in enumerate(a):
    if x in v:
        v[x].append(i)
    else:
        v[x] = [i]
for (x, li) in list(v.items()):
    if len(li) == 1:
        w.append((x, 0))
    else:
        d = li[1] - li[0]
        sign = True
        for i in range(1, len(li)):
            if li[i] - li[i - 1] != d:
                sign = False
        if sign:
            w.append((x, d))
print(len(w))
print('\n'.join(('%d %d' % x for x in sorted(w))))

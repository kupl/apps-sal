(h, w) = map(int, input().split())
ab = list((input() for _ in range(h)))
res = []
for i in range(h):
    if ab[i].count('.') == w:
        pass
    else:
        res.append(ab[i])
l = len(res)
ress = []
for j in range(w):
    b = list(map(lambda x: x[j], res))
    if b.count('.') == l:
        pass
    else:
        ress.append(b)
ans = list(zip(*ress))
for i in range(l):
    print(''.join(ans[i]))

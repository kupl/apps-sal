n, k, m = map(int, input().split(' '))
lw = list(input().split(' '))
lp = list(map(int, input().split(' ')))
for i in range(k):
    tl = list(map(lambda x: int(x) - 1, input().split(' ')))
    tl.pop(0)
    tpl = list()
    for i in tl:
        tpl.append(lp[i])
    m = min(tpl)
    for i in tl:
        lp[i] = m
el = list(input().split(' '))
d = dict()
for i in range(n):
    d[lw[i]] = lp[i]
s = 0
for i in el:
    s += d[i]
print(s)

from itertools import groupby
def R(): return map(int, input().split())


x, k = R()
a = [0] * (x - 1)
for _ in range(k):
    l = list(R())
    if l[0] == 1:
        a[l[2] - 1] = 1
    a[l[1] - 1] = 1
b = [len(list(g)) for k, g in groupby(a) if k == 0]
x = y = 0
for l in b:
    x += l // 2 + l % 2
    y += l
print(x, y)

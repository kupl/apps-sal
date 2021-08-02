from itertools import groupby
R = lambda: map(int, input().split())
x, k = R()
a = [0] * (x - 1)
for _ in range(k):
    l = list(R())
    if l[0] == 1:
        a[l[2] - 1] = 1
    a[l[1] - 1] = 1
b = [len(list(g)) for k, g in groupby(a) if k == 0]
print(sum(l // 2 + l % 2 for l in b), sum(b))

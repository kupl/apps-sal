import itertools
N = int(input())
v = list(map(int, input().split()))
for _ in range(N - 1):
    c = list(itertools.combinations(v, 2))
    x = 10000
    idx = None
    for (i, j) in enumerate(c):
        a = (j[0] + j[1]) / 2
        if x > a:
            x = a
            idx = i
    n = v.index(c[idx][0])
    v.pop(n)
    m = v.index(c[idx][1])
    v.pop(m)
    v.append(x)
print(v[0])

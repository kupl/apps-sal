n = int(input())
a = list(map(int, input().split()))
d = [0] * 3


def update(u):
    for i in u:
        d[i] += 1


MEX = {(0, 0): 1, (0, 1): 2, (0, 2): 1, (1, 1): 0, (1, 2): 0, (2, 2): 0}


def mex(u, v):
    return MEX[min(u, v), max(u, v)]


def proc(v):
    u = [int(input())]
    for i in range(1, len(v)):
        u.append(mex(u[-1], v[i]))
    return u


update(a)
for _ in range(2, min(5, n + 1)):
    a = proc(a)
    update(a)
for j in range(4, n):
    d[a[j - 1]] += n - j
a = a[:4]
for i in range(5, n + 1):
    a = proc(a)
    update(a)
    d[a[3]] += n - i
print(*d)

from bisect import bisect_left as bl
c = []


def gen(n, nz):
    if len(n) >= 19:
        return
    nonlocal c
    c.append(int(n))
    if nz == 3:
        n += "0"
        gen(n, nz)
        return
    gen(n + "0", nz)
    for i in ("123456789"):
        gen(n + i, nz + 1)


for i in ("123456789"):
    gen(i, 1)
c.append(10**18)
c.sort()
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    x = min(bl(c, b), len(c) - 1)
    y = bl(c, a)
    if x == y and b < c[x]:
        print(0)
    elif (c[x] == b and c[y] == a) or c[x] == b:
        print(x - y + 1)
    else:
        print(x - y)

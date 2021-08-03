from math import ceil


def check(p):
    sm = 0
    k = 0
    d = 0
    for i in range(ceil(len(a) / p)):
        for j in range(p):
            if k < len(a):
                sm += max(0, a[k] - d)
                k += 1
        d += 1
    return sm >= m


n, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
a.sort(reverse=True)

l = 1
r = len(a)
if sum(a) < m:
    print(-1)
else:
    while(l < r):
        mid = (l + r) // 2

        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(l)

n, k = map(int, input().split())
if k % 2 == 0:
    print(-1); return()
k -= 1
a = [int(i + 1) for i in range(n)]


def f(l, r):
    nonlocal k
    if k < 2 or r - l < 2:
        return
    k -= 2
    m = (l + r) // 2
    a[m], a[m - 1] = a[m - 1], a[m]
    f(l, m)
    f(m, r)


f(0, n)
if k: print(-1); return()
for i in a:
    print(int(i), end=' ')

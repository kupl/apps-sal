n, k = map(int, input().split())
if k % 2 == 0:
    print(-1)
    return()
k -= 1
a = [i + 1 for i in range(n)]


def sl(l, r):
    nonlocal k
    if r - l < 2 or k == 0:
        return
    k -= 2
    m = (l + r) // 2
    a[m], a[m - 1] = a[m - 1], a[m]
    sl(l, m)
    sl(m, r)


sl(0, n)
if k != 0:
    print(-1)
    return()
print(' '.join([str(i) for i in a]))

def f(ii, i0, i1):
    nonlocal xy
    rtn = []
    x0, y0 = xy[i0]
    x1, y1 = xy[i1]
    for i in ii:
        xi, yi = xy[i]
        if (xi - x0) * (yi - y1) != (xi - x1) * (yi - y0):
            rtn.append(i)
    return rtn


def g(i0, i1):
    nonlocal f, n
    ls = f(list(range(n)), i0, i1)
    if len(ls) <= 2:
        return -1
    else:
        rs = f(ls, ls[0], ls[-1])
        if len(rs) == 0:
            return -1
        else:
            return rs[0]


n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = "NO"
if n <= 4:
    ans = "YES"
else:
    xy.sort()
    i = g(0, n - 1)
    if i < 0:
        ans = "YES"
    elif g(0, i) < 0:
        ans = "YES"
    elif g(n - 1, i) < 0:
        ans = "YES"
print(ans)

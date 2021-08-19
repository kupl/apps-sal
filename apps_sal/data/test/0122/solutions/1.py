def solve():
    n = int(input())
    #n, w = map(int, input().split())
    a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    ok = 0
    Su = sum(a)
    di = dict()
    di[0] = 1
    su = 0
    for i in range(n):
        su += a[i]
        if di.get(a[i] * 2, 0) == 0:
            di[a[i] * 2] = 1
        if di.get(su - Su + su, 0) == 0:
            pass
        else:
            ok = 1
    di.clear()
    di[0] = 1
    su = 0
    for i in range(-1, -n - 1, -1):
        su += a[i]
        if di.get(a[i] * 2, 0) == 0:
            di[a[i] * 2] = 1
        if di.get(su - Su + su, 0) == 0:
            pass
        else:
            ok = 1
    if ok:
        print('YES')
    else:
        print('NO')


def __starting_point():
    solve()


__starting_point()

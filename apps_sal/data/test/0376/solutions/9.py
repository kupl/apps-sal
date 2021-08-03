import sys


def solve():
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    s = [[] for g in d]
    mx_tmp = max(d)
    mx_tmp2 = max(g for g in d + [-2e9] if g < mx_tmp)
    mxpt = [mx_tmp, mx_tmp2]
    mxcnt = [d.count(mx_tmp), d.count(mx_tmp2)]
    for i in range(1, n):
        a, b = map(int, sys.stdin.readline().split())

        a -= 1
        b -= 1
        s[a] += [b]
        s[b] += [a]

    mx = int(2e9)
    for i in range(n):
        nmx = [] + mxcnt
        tmpmax = d[i]
        for k in s[i]:
            if d[k] == mxpt[0]:
                nmx[0] -= 1
            elif d[k] == mxpt[1]:
                nmx[1] -= 1

        if nmx[0] != mxcnt[0]:
            tmpmax = mxpt[0] + 1
        elif nmx[1] != mxcnt[1]:
            tmpmax = max(tmpmax, mxpt[1] + 1)

        if d[i] == mxpt[0]:
            nmx[0] -= 1
        elif d[i] == mxpt[1]:
            nmx[1] -= 1

        if nmx[0]:
            tmpmax = mxpt[0] + 2
        elif nmx[1]:
            tmpmax = max(mxpt[1] + 2, tmpmax)
        mx = min(mx, tmpmax)
    print(mx)


def __starting_point():
    solve()


__starting_point()

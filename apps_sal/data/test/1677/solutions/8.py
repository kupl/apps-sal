import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    a = [None] * n
    i = 0
    for v in mints():
        a[i] = (v, i)
        i += 1
    a.sort()
    i = 0
    r = 0
    while i < n:
        j = i + 1
        x = a[i][0]
        while j < n and a[j][0] == x:
            j += 1
        r = max(r, j - i)
        ni = j
        while j < n:
            jj = j
            y = a[j][0]
            ii = i
            if a[ii][1] < a[jj][1]:
                cnt = 1
                left = a[ii][1]
                ii += 1
            else:
                cnt = 0
                left = -1
            fail = False
            while True:
                while True:
                    if jj >= n or a[jj][0] != y:
                        fail = True
                        break
                    if a[jj][1] > left:
                        left = a[jj][1]
                        cnt += 1
                        jj += 1
                        break
                    jj += 1
                if fail:
                    break
                while True:
                    if ii >= ni:
                        fail = True
                        break
                    if a[ii][1] > left:
                        left = a[ii][1]
                        cnt += 1
                        ii += 1
                        break
                    ii += 1
                if fail:
                    break
            r = max(r, cnt)
            while jj < n and a[jj][0] == y:
                jj += 1
            j = jj
        i = ni
    print(r)


solve()

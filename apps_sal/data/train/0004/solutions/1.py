import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n = int(I())
    l = list(map(int, I().split()))
    r = list(range(n))
    r.sort(key=lambda x: l[x])
    (mn, mx) = (None, None)
    for i in range(n):
        if mn is None:
            mn = mx = r[i]
        else:
            mn = min(mn, r[i])
            mx = max(mx, r[i])
        l[i] = '1' if mx - mn == i else '0'
    print(''.join(l))

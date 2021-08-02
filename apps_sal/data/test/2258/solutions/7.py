import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def issorted(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            return False
    return True


n = mint()
a = list(mints())
inv = []
for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]: inv.append((i, -a[j], -j))
inv.sort(reverse=True)
r = list(range(len(inv)))
if r is not None:
    print(len(r))
    for z in r: v, _, u = inv[z]; u = -u; print(u + 1, v + 1)
else:
    print("wut")

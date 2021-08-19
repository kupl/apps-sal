from sys import stdin
input = stdin.readline


def myk(l, stops, czas):
    pos = 0
    v = 1.0
    for stop in stops:
        dist = stop - pos
        if czas * v > dist:
            czas -= dist / v
            pos = stop
            v += 1
        else:
            return pos + czas * v
    return pos + czas * v


def solve():
    (n, l) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [l - x for x in a[::-1]]
    pocz = 0.0
    kon = l / 2.0
    eps = 1e-07
    while pocz + eps < kon:
        mid = (pocz + kon) / 2.0
        pos1 = myk(l, a, mid)
        pos2 = l - myk(l, b, mid)
        if pos1 < pos2:
            pocz = mid
        else:
            kon = mid
    print(kon)


t = int(input())
for _ in range(t):
    solve()

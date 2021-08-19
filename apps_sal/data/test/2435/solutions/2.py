import sys
readline = sys.stdin.readline
read = sys.stdin.read


def ns():
    return readline().rstrip()


def ni():
    return int(readline().rstrip())


def nm():
    return map(int, readline().split())


def nl():
    return list(map(int, readline().split()))


def prn(x):
    return print(*x, sep='\n')


def solve():
    (n, x, m) = nm()
    l = r = x
    for _ in range(m):
        (p, q) = nm()
        if p <= l <= q:
            l = p
        if p <= r <= q:
            r = q
    print(r - l + 1)
    return


T = ni()
for _ in range(T):
    solve()

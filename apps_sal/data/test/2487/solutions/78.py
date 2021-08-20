import sys
readline = sys.stdin.readline
readall = sys.stdin.read


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
    n = ni()
    ans = 0
    for i in range(1, n + 1):
        ans += i * (n - i + 1)
    for _ in range(n - 1):
        (u, v) = nm()
        if u > v:
            (u, v) = (v, u)
        ans -= u * (n - v + 1)
    print(ans)
    return


solve()

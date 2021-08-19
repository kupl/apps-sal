import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines


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


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def solve():
    (m, d, w) = nm()
    g = w // gcd(d - 1, w)
    c = min(m, d)
    v = c // g
    ans = v * (v - 1) // 2 * g
    ans += (c - g * v) * v
    print(ans)
    return


T = ni()
for _ in range(T):
    solve()

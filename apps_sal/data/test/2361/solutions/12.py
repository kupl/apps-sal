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


def solve():
    (n, m, k) = nm()
    if n // k >= m:
        print(m)
        return
    else:
        m -= n // k
        print(n // k - (m - 1) // (k - 1) - 1)
    return


T = ni()
for _ in range(T):
    solve()

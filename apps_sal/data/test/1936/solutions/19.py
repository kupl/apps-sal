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
    (a, b) = nm()
    if a * 2 > b:
        print(-1, -1)
    else:
        print(a, 2 * a)
    return


T = ni()
for _ in range(T):
    solve()

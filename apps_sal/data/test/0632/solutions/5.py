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
    (n, k) = nm()
    for i in range(2, n + 1):
        if n % i == 0:
            n += i
            break
    n += 2 * (k - 1)
    print(n)
    return


T = ni()
for _ in range(T):
    solve()

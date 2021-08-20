import sys
import math
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
    n = ni()
    print(1 / math.tan(math.pi / (2 * n)))
    return


T = ni()
for _ in range(T):
    solve()

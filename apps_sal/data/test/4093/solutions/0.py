import sys
input = sys.stdin.readline


def rInt():
    return int(input())


def mInt():
    return list(map(int, input().split()))


def rLis():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    (n, m) = mInt()
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2 * m)

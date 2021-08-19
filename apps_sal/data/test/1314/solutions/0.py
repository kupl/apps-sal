import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


n = int(input())
a = 0
b = 0
for _ in range(2 * n):
    (u, v) = mii()
    a += u
    b += v
print('%d %d' % (a // n, b // n))

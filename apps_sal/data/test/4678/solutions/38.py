import sys
from sys import stdin


def I():
    return stdin.readline().rstrip()


def MI():
    return map(int, stdin.readline().rstrip().split())


def LI():
    return list(map(int, stdin.readline().rstrip().split()))


n = int(I())
a = LI()
ans = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        ans += a[i] - a[i + 1]
        a[i + 1] = a[i]
print(ans)

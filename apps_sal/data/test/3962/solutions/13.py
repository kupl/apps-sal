import sys


def rint():
    return map(int, sys.stdin.readline().split())


n = int(input())
r = [0] * n
l = [0] * n

for i in range(n):
    r[i], l[i] = rint()

r.sort()
l.sort()

ans = 0

for i in range(n):
    ans += max(r[i], l[i])

print(ans + n)

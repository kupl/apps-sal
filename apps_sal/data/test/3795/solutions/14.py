import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))


n = int(input())
d = int(input())
e = int(input())

d_min = d
e_min = 5 * e

min1, min2 = sorted([d_min, e_min])

ans = 10**10
for i in range(0, min1 + 1):
    tmp = n - i * min2
    if tmp < 0:
        break
    tmp = tmp % min1
    ans = min(tmp, ans)

print(ans)

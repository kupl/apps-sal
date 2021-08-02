import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def lis(): return [int(i) for i in input().split()]
def value(): return int(input())


a1 = value()
a2 = value()
k1 = value()
k2 = value()
n = value()
if k1 > k2:
    k1, k2 = k2, k1
    a1, a2 = a2, a1
tot = 0
temp = n
if n > a1 * k1:
    tot += a1
    n -= a1 * k1
    if n > a2 * k2:
        tot += a2
    else:
        tot += n // k2
else:
    tot += n // k1

ans1 = tot
tot = 0
n = temp
n -= (k1 - 1) * a1
n -= (k2 - 1) * a2
if n > 0:
    ans2 = min(a1 + a2, n)
else:
    ans2 = 0

print(min(ans1, ans2), max(ans2, ans1))

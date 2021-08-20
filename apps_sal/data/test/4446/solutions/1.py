from sys import stdin
input = stdin.readline
(n, a, b, k) = map(int, input().split())
l = list(map(int, input().split()))


def cost(h):
    h -= (a + b) * ((h - (a + b)) // (a + b))
    if h > a + b:
        h -= a + b
    return (h - 1) // a


pyk = []
for i in range(n):
    pyk.append(cost(l[i]))
pyk.sort()
wyn = 0
su = 0
for i in range(n):
    su += pyk[i]
    if su <= k:
        wyn += 1
print(wyn)

from math import *


def rr(t):
    zzz = [t(i) for i in input().split()]
    if len(zzz) == 1:
        return zzz[0]
    return zzz


def r3(t):
    return [t(i) for i in input()]


k = int(input())
cnt = 1
s = [i for i in 'codeforces']
ts = [1 for i in s]
ci = 0
while cnt < k:
    cnt = cnt * (ts[ci] + 1) // ts[ci]
    ts[ci] += 1
    ci = (ci + 1) % len(s)

for i in range(len(ts)):
    print(s[i] * ts[i], end='')
print()

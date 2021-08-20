import sys


def minp():
    return sys.stdin.readline().strip()


dp = [None] * 50
for j in range(50):
    dp[j] = [None] * 2001
(n, s, k) = list(map(int, minp().split()))
a = [None] * n
i = 0
s -= 1
for j in map(int, minp().split()):
    a[i] = (j, i)
    i += 1
i = 0
for j in minp():
    a[i] += ('RGB'.find(j),)
    i += 1
a.sort()
r = 10 ** 18
zzz = 0
for i in range(n):
    ii = dp[i]
    c = a[i][0]
    ii[c] = abs(s - a[i][1])
    for j in range(i):
        if a[j][2] == a[i][2] or a[j][0] == a[i][0]:
            continue
        jj = dp[j]
        for z in range(2001 - c):
            zz = jj[z]
            if zz != None:
                d = zz + abs(a[i][1] - a[j][1])
                cc = z + c
                if ii[cc] != None:
                    if ii[cc] > d:
                        ii[cc] = d
                else:
                    ii[cc] = d
    for z in range(k, 2001):
        if ii[z] != None:
            r = min(r, ii[z])
if r != 10 ** 18:
    print(r)
else:
    print(-1)

from sys import stdin
from sys import setrecursionlimit as SRL
SRL(10 ** 7)
rd = stdin.readline


def rrd():
    return list(map(int, rd().strip().split()))


s = str(rd().strip())
ans = [[0] * 11 for _j in range(11)]
ddp = [[[100000] * 11 for _k in range(11)] for kk in range(11)]
tt = [0] * 11
for i in range(10):
    for j in range(10):
        for u in range(11):
            for v in range(11):
                if u == 0 and v == 0:
                    continue
                k = (i * u + j * v) % 10
                ddp[i][j][k] = min(ddp[i][j][k], max(0, u + v - 1))
pre = 0
for i in range(1, len(s)):
    t = (int(s[i]) + 10 - pre) % 10
    tt[t] += 1
    pre = int(s[i])
for i in range(10):
    asi = ''
    for j in range(10):
        for k in range(11):
            if tt[k] and ddp[i][j][k] >= 80000:
                ans[i][j] = -1
                break
            ans[i][j] += tt[k] * ddp[i][j][k]
        asi = asi + str(ans[i][j]) + ' '
    print(asi)

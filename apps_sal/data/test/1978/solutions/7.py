from sys import stdin
from sys import setrecursionlimit as SRL
SRL(10 ** 7)
rd = stdin.readline


def rrd():
    return map(int, rd().strip().split())


dis = [[1000000000] * 101 for _i in range(101)]
n = int(rd())
for i in range(n + 1):
    dis[i][i] = 0
for i in range(1, n + 1):
    s = str(rd().strip())
    for j in range(n):
        if s[j] == '1':
            dis[i][j + 1] = 1
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
m = int(rd())
p = list(rrd())
ans = []
s = 0
pre = 0
l = 0
for i in p:
    if len(ans) == 0:
        s = i
        pre = i
        ans.append(i)
        continue
    if dis[s][i] == l + 1:
        pre = i
        l += 1
        continue
    else:
        ans.append(pre)
        s = pre
        pre = i
        l = 1
if s != pre:
    ans.append(pre)
print(len(ans))
print(*ans)

from sys import stdin, stdout
from sys import setrecursionlimit as SRL
SRL(10**7)
rd = stdin.readline
def rrd(): return map(int, rd().strip().split())


nxt = [0] * (1000005)
n = int(rd())

s = list(rd().split())

ans = []
for i in s[0]:
    ans.append(i)

for i in range(1, n):

    v = s[i]

    t = 0

    for i in range(2, len(v)):
        while t and v[i - 1] != v[t]:
            t = nxt[t]
        if v[i - 1] == v[t]:
            t += 1
        nxt[i] = t

    t = 0
    for i in range(max(0, len(ans) - len(v)), len(ans)):
        while t and ans[i] != v[t]:
            t = nxt[t]
        if ans[i] == v[t]:
            t += 1

    while t < len(v):
        ans.append(v[t])
        t += 1


print("".join(ans) + '\n')

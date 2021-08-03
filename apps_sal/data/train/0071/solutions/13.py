from sys import stdin
from math import ceil
def inp(): return stdin.readline().strip()


t = int(inp())

for _ in range(t):
    n = int(inp())
    a = [int(x) for x in inp().split()]
    cumm = 0
    ans = 0
    for i in range(n):
        cumm += a[i]
        if cumm < 0:
            ans = min(ans, cumm)
    print(-1 * ans)

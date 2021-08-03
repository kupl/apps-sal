from bisect import bisect_right
import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())


sys.setrecursionlimit(10**9)

N = int(input())
ab = [list(mapint()) for _ in range(N)]
cd = [list(mapint()) for _ in range(N)]
ab.sort(reverse=True)
cd.sort(key=lambda x: x[1])
checked = [0] * N

ans = 0
for n in range(N):
    a, b = ab[n]
    for i in range(N):
        if checked[i]:
            continue
        c, d = cd[i]
        if a < c and b < d:
            ans += 1
            checked[i] = 1
            break

print(ans)

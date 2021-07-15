import sys
N = int(input())
Er = set(range(1, N+1))
for i in range(1, N + 1):
    p, c = map(int, sys.stdin.readline().split())
    if c == 0:
        if i in Er:
            Er.remove(i)
        if p in Er:
            Er.remove(p)
Er = list(Er)
if not Er:
    print(-1)
else:
    Er.sort()
    print(*Er)

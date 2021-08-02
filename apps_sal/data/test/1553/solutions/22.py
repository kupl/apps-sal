import sys

n, h = map(int, input().split())
l = list(map(int, sys.stdin.readline().split()))
c = l.copy()
i = 0
c.sort(reverse=True)
T = float('infinity')
while T > h:
    T = sum([c[k] for k in range(0, n - i, 2)])
    c.pop(c.index(l[-i - 1]))
    i += 1
print(n + 1 - i)

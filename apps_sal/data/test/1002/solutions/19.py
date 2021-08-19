import sys
f = sys.stdin
(n, d) = map(int, f.readline().strip().split())
t = list(map(int, f.readline().strip().split()))
s = sum(t)
if 10 * (n - 1) + s > d:
    print(-1)
else:
    jokes = 0
    d -= s
    print(d // 5)

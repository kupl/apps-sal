import sys
input = sys.stdin.readline
print = sys.stdout.write
(n, q) = map(int, input().split())
ar = list(map(int, input().split()))
qs = [map(int, input().split()) for x in range(q)]
s = [0] * n


def f(l, r):
    s[l] += 1
    if r < n:
        s[r] -= 1


for x in range(q):
    (a, b) = qs[x]
    a -= 1
    f(a, b)
d = [s[0]]
for x in range(1, n):
    s[x] += s[x - 1]
    d.append(s[x])
ar = sorted(ar)
d = sorted(d)[::-1]
sm = 0
for x in range(n):
    sm += ar[x] * d[n - x - 1]
print(str(sm))

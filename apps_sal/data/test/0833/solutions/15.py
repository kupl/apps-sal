import sys
f = sys.stdin
n, v = list(map(int, f.readline().strip().split()))

p = [0] * 3002
for i in range(n):
    a, b = list(map(int, f.readline().strip().split()))
    p[a] += b
S = 0
for k in range(1, len(p)):
    dv = min(v, p[k - 1])
    S += dv
    p[k - 1] -= dv

    dv = min(v - dv, p[k])
    S += dv
    p[k] -= dv
print(S)

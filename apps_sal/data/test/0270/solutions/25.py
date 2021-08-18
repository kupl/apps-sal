import sys
input = sys.stdin.readline

N, M = map(int, input().split())
u = [[] for i in range(N - 1)]
for i in range(M):
    s, t = map(int, input().split())
    u[s - 1].append(t - 1)

p = [0] * N
p[0] = 1
for x, y in enumerate(u):
    for z in y:
        p[z] += p[x] / len(y)

q = [0] * N
q[N - 1] = 0
for x, y in list(enumerate(u))[::-1]:
    q[x] = sum(q[z] for z in y) / len(y) + 1

v = [0] * N
for i in range(N - 1):
    a = len(u[i])
    if a > 1:
        b = max(q[c] for c in u[i])
        v[i] = p[i] * (q[i] - (1 + b)) / (a - 1)

print(q[0] + min(v))

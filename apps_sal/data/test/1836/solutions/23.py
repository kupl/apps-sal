import sys

# sys.stdin = open("ivo.in")

n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)

neighbours = []
ne = []
smaller = []
for i in range(n):
    neighbours.append(0)
    smaller.append(1)
    ne.append([])


for i in range(m):
    f, t = sys.stdin.readline().split()
    f = int(f) - 1
    t = int(t) - 1
    neighbours[f] += 1
    neighbours[t] += 1
    if f < t:
        ne[f].append(t)
    else:
        ne[t].append(f)


for i in range(n):
    for sysed in ne[i]:
        smaller[sysed] = max([smaller[sysed], smaller[i] + 1])

ans = 0
for i in range(n):
    ans = max([ans, smaller[i] * neighbours[i]])

print(ans)
